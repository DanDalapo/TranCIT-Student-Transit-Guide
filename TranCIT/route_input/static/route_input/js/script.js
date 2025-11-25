document.addEventListener('DOMContentLoaded', () => {
    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => document.querySelectorAll(sel);

    const routeForm = $('#routeForm');
    const originInput = $('#id_origin');
    const destinationInput = $('#id_destination');
    const suggestionsContainer = $('#destinationSuggestions');
    const transportSelect = $('#id_transport_type');
    const calculatedFareEl = $('#calculatedFare');
    const calculatedTimeEl = $('#calculatedTime');
    const calculatedDistanceEl = $('#calculatedDistance');
    const calculatedTransportEl = $('#calculatedTransport');
    const fareInput = $('#id_fare');
    const distInput = $('#id_distance_km');
    const timeInput = $('#id_travel_time_minutes');
    const originLat = $('#id_origin_latitude');
    const originLon = $('#id_origin_longitude');
    const destLat = $('#id_destination_latitude');
    const destLon = $('#id_destination_longitude');
    const codeInput = $('#id_code'); 
    const notesInput = $('#id_notes');
    const detectBtn = $('#detectLocationBtn');
    const saveMyRouteBtn = $('#saveMyRouteBtn');
    const pinOriginBtn = $('#pinOriginBtn');
    const pinDestinationBtn = $('#pinDestinationBtn');
    const navigateBtn = $('#navigateBtn');
    const resetFormBtn = $('#resetFormBtn');
    
    const helpBtn = $('#helpBtn');
    const tutorialOverlay = $('#tutorialOverlay');
    const tutorialTitle = $('#tutorialTitle');
    const tutorialText = $('#tutorialText');
    const tutorialSteps = $('#tutorialSteps');
    const tutorialIndicator = $('#tutorialIndicator');
    const nextTutorialBtn = $('#nextTutorial');
    const skipTutorialBtn = $('#skipTutorial');

    const mapIframe = $('#map-container iframe');
    let foliumMap; 
    let L_Leaflet; 
    
    // State Variables
    let currentRouteLayer = null;   
    let currentActiveButton = null; 

    const csrftoken = document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1];

    const alertMsg = (msg) => typeof showNotification === 'function' ? showNotification(msg) : alert(msg);
    
    const qs = (params) => new URLSearchParams(params).toString();

    const postJSON = async (url, data) => {
        const res = await fetch(url, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            body: data
        });
        return res.json();
    };

    const updateURL = (params) => {
        const newUrl = `${window.location.pathname}?${qs(params)}`;
        window.history.replaceState({}, '', newUrl);
    };
    
    function getMapObjects() {
        if (foliumMap && L_Leaflet) return true; 
        if (mapIframe && mapIframe.contentWindow) {
            if (mapIframe.contentWindow.map) foliumMap = mapIframe.contentWindow.map;
            if (mapIframe.contentWindow.L) L_Leaflet = mapIframe.contentWindow.L;
        }
        return foliumMap && L_Leaflet;
    }
    setTimeout(getMapObjects, 1500);

    function toggleNavigateButton() {
        const hasOrigin = originLat.value && originLon.value;
        const hasDestination = destLat.value && destLon.value;
        navigateBtn.disabled = !(hasOrigin && hasDestination);
        navigateBtn.style.opacity = (hasOrigin && hasDestination) ? 1 : 0.6;
        navigateBtn.style.cursor = (hasOrigin && hasDestination) ? 'pointer' : 'not-allowed';
    }
    setInterval(toggleNavigateButton, 1000);

    function syncInputsFromURL() {
        const params = new URLSearchParams(window.location.search);
        if (params.has('origin_latitude')) originLat.value = params.get('origin_latitude');
        if (params.has('origin_longitude')) originLon.value = params.get('origin_longitude');
        if (params.has('destination_latitude')) destLat.value = params.get('destination_latitude');
        if (params.has('destination_longitude')) destLon.value = params.get('destination_longitude');
        if (params.has('origin_text')) originInput.value = decodeURIComponent(params.get('origin_text'));
        if (params.has('destination_text')) destinationInput.value = decodeURIComponent(params.get('destination_text'));
        toggleNavigateButton();
    }
    syncInputsFromURL();
    window.addEventListener('load', syncInputsFromURL);

    function sendPinCommand(mode) {
        const iframe = document.querySelector('#map-container iframe');
        if (!iframe?.contentWindow) return alertMsg('Map not ready yet. Please wait.');
        
        const params = new URLSearchParams(window.location.search);
        if (mode === 'origin' && destLat.value) {
            params.set('destination_latitude', destLat.value);
            params.set('destination_longitude', destLon.value);
            params.set('destination_text', destinationInput.value);
        } else if (mode === 'destination' && originLat.value) {
            params.set('origin_latitude', originLat.value);
            params.set('origin_longitude', originLon.value);
            params.set('origin_text', originInput.value);
        }
        updateURL(params);
        iframe.contentWindow.postMessage({ type: 'SET_PIN_MODE', mode }, '*');
        
        const niceMode = mode.charAt(0).toUpperCase() + mode.slice(1);
        alertMsg(`Click anywhere on the map to set ${niceMode}`);
    }
    pinOriginBtn?.addEventListener('click', () => sendPinCommand('origin'));
    pinDestinationBtn?.addEventListener('click', () => sendPinCommand('destination'));

    navigateBtn?.addEventListener('click', (e) => {
        e.preventDefault();

        if (!transportSelect.value) {
            transportSelect.classList.add('input-error');
            transportSelect.addEventListener('change', () => { transportSelect.classList.remove('input-error'); }, { once: true });
            return alertMsg('Please choose a transport type.');
        }
        if (!originLat.value || !destLat.value) return alertMsg('Please pin both origin and destination.');
        if (!getMapObjects()) return alertMsg('Map is not ready yet.');

        navigateBtn.disabled = true;
        navigateBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Calculating...';

        const routeData = {
            origin_latitude: originLat.value,
            origin_longitude: originLon.value,
            destination_latitude: destLat.value,
            destination_longitude: destLon.value,
            origin_text: originInput.value,
            destination_text: destinationInput.value,
            transport_type: transportSelect.value
        };

        fetch('/routes/get_route_data/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
            body: JSON.stringify(routeData)
        })
        .then(r => r.json())
        .then(data => {
            if (data.error) throw new Error(data.error);

            fareInput.value = data.fare.toFixed(2);
            distInput.value = data.distance_km.toFixed(2);
            timeInput.value = data.travel_time_minutes.toFixed(2);
            
            calculatedFareEl.textContent = `Php ${data.fare.toFixed(2)}`;
            calculatedTimeEl.textContent = `${data.travel_time_minutes.toFixed(0)} min`;
            calculatedDistanceEl.textContent = `${data.distance_km.toFixed(1)} km`;
            calculatedTransportEl.textContent = routeData.transport_type;

            drawNavigatedRoute(data.path_coords, routeData);

            navigateBtn.innerHTML = '<i class="fa-solid fa-route"></i> Navigate Route';
            toggleNavigateButton();
            if (saveMyRouteBtn) saveMyRouteBtn.disabled = false;
        })
        .catch(err => {
            console.error(err);
            alertMsg(`Error: ${err.message}`);
            navigateBtn.innerHTML = '<i class="fa-solid fa-route"></i> Navigate Route';
            toggleNavigateButton();
        });
    });

    function clearCurrentRoute() {
        if (currentRouteLayer) {
            foliumMap.removeLayer(currentRouteLayer);
            currentRouteLayer = null;
        }
        if (currentActiveButton) {
            const isSaved = currentActiveButton.classList.contains('view-saved-route');
            const originalText = isSaved ? 'View' : 'View Route';
            currentActiveButton.innerHTML = `<i class="fa-solid fa-map"></i> ${originalText}`;
            currentActiveButton.classList.remove('viewing');
            currentActiveButton = null;
        }
    }

    function drawNavigatedRoute(pathCoords, routeData) {
        if (!getMapObjects()) return;
        clearCurrentRoute(); 

        try {
            const polyline = L_Leaflet.polyline(pathCoords, { color: '#2B86C3EE', weight: 8, opacity: 0.8 });
            
            const originIcon = L_Leaflet.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'blue' });
            const destIcon = L_Leaflet.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'red' });

            const originMarker = L_Leaflet.marker([routeData.origin_latitude, routeData.origin_longitude], {icon: originIcon}).bindPopup(routeData.origin_text || "Origin");
            const destMarker = L_Leaflet.marker([routeData.destination_latitude, routeData.destination_longitude], {icon: destIcon}).bindPopup(routeData.destination_text || "Destination");

            const layerGroup = L_Leaflet.featureGroup([polyline, originMarker, destMarker]);
            layerGroup.addTo(foliumMap);
            foliumMap.fitBounds(layerGroup.getBounds().pad(0.1));
            currentRouteLayer = layerGroup;
        } catch (err) {
            console.error(err);
            alertMsg('Error displaying route on map.');
        }
    }

    const saveSuggestionsContainer = $('#dynamicSuggestions');
    if (saveSuggestionsContainer) {
        saveSuggestionsContainer.addEventListener('click', (e) => {
            const saveButton = e.target.closest('.save-suggested-route');
            const viewButton = e.target.closest('.view-suggested-route');
            if (saveButton) {
                const routeId = saveButton.dataset.routeId;
                const formData = new FormData();
                formData.append('route_id', routeId);
                performSave('/routes/save_suggested_route/', formData);
            }
            if (viewButton) handleViewRouteClick(viewButton);
        });
    }

    const savedListContainer = $('#savedList');
    if (savedListContainer) {
        savedListContainer.addEventListener('click', (e) => {
            const deleteButton = e.target.closest('.delete-saved-route');
            const viewButton = e.target.closest('.view-saved-route');
            if (deleteButton) {
                const savedId = deleteButton.dataset.savedId;
                if (confirm('Delete this route?')) {
                    const formData = new FormData();
                    formData.append('saved_id', savedId);
                    const el = deleteButton.closest('.saved-route-item');
                    performDelete('/routes/delete_saved_route/', formData, el);
                }
            }
            if (viewButton) handleViewRouteClick(viewButton);
        });
    }

    function handleViewRouteClick(button) {
        if (!getMapObjects()) return alertMsg('Map is not ready.');
        
        if (currentActiveButton === button) {
            clearCurrentRoute();
            return;
        }
        if (currentActiveButton) {
            clearCurrentRoute();
        }

        const ds = button.dataset;
        if (!ds.path || ds.path.length < 3) return alertMsg('Error: No path data.');

        try {
            const pathCoords = JSON.parse(ds.path);
            const polyline = L_Leaflet.polyline(pathCoords, { color: 'purple', weight: 4, opacity: 0.8 });
            
            let originMarker, destMarker;
            try {
                const oIcon = L_Leaflet.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'blue' });
                const dIcon = L_Leaflet.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'red' });
                originMarker = L_Leaflet.marker([ds.originLat, ds.originLon], {icon: oIcon}).bindPopup("Origin");
                destMarker = L_Leaflet.marker([ds.destLat, ds.destLon], {icon: dIcon}).bindPopup("Destination");
            } catch(e) {
                originMarker = L_Leaflet.marker([ds.originLat, ds.originLon]);
                destMarker = L_Leaflet.marker([ds.destLat, ds.destLon]);
            }

            const layerGroup = L_Leaflet.featureGroup([polyline, originMarker, destMarker]);
            layerGroup.addTo(foliumMap);
            foliumMap.fitBounds(layerGroup.getBounds().pad(0.1));

            currentRouteLayer = layerGroup;
            currentActiveButton = button;

            const unviewText = button.classList.contains('view-saved-route') ? 'Unview' : 'Unview Route';
            button.innerHTML = `<i class="fa-solid fa-eye-slash"></i> ${unviewText}`;
            button.classList.add('viewing');
        } catch (err) {
            console.error(err);
            alertMsg('Error displaying route.');
        }
    }

    async function performSave(url, formData) {
        if (!csrftoken) return alertMsg('Error: CSRF token not found.');
        const res = await fetch(url, { method: 'POST', headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' }, body: formData });
        const data = await res.json();
        if (res.ok) { alertMsg(data.message); window.location.reload(); }
        else alertMsg('Error: ' + data.error);
    }

    async function performDelete(url, formData, el) {
        if (!csrftoken) return alertMsg('Error: CSRF token not found.');
        const res = await fetch(url, { method: 'POST', headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' }, body: formData });
        const data = await res.json();
        if (res.ok) { el.style.opacity = '0'; setTimeout(() => el.remove(), 300); }
        else alertMsg('Error: ' + data.error);
    }

    // === 7. TUTORIAL LOGIC (FIXED) ===
    const tutorialStepsData = [
      { title: "Welcome to TranCIT! 🚍", text: "TranCIT helps you navigate Cebu City. Let's show you around!", highlight: null },
      { title: "Plan Your Route", text: "Enter details in the left panel.", highlight: ".sidebar" },
      { title: "Interactive Map", text: "The map shows your route and stops.", highlight: ".map-area" },
      { title: "Helpful Suggestions", text: "See jeepney routes and suggestions on the right.", highlight: ".suggestions" },
      { title: "You're All Set!", text: "Click Help anytime to see this again.", highlight: null }
    ];

    let currentStep = 0;

    function showTutorialStep(step) {
        const data = tutorialStepsData[step];
        $$('.highlight-pulse').forEach(el => el.classList.remove('highlight-pulse'));
        
        tutorialTitle.textContent = data.title;
        tutorialText.textContent = data.text;
        tutorialIndicator.textContent = `Step ${step + 1} of ${tutorialStepsData.length}`;

        if (data.highlight) {
            const el = document.querySelector(data.highlight);
            if (el) el.classList.add('highlight-pulse');
        }

        nextTutorialBtn.textContent = (step === tutorialStepsData.length - 1) ? 'Finish' : 'Next';
    }

    function startTutorial() {
        currentStep = 0;
        tutorialOverlay.classList.add('active');
        showTutorialStep(0);
    }

    function closeTutorial() {
        tutorialOverlay.classList.remove('active');
        $$('.highlight-pulse').forEach(el => el.classList.remove('highlight-pulse'));
        localStorage.setItem('trancit_tutorial_seen', 'true');
    }

    if (nextTutorialBtn) {
        nextTutorialBtn.addEventListener('click', () => {
            if (currentStep < tutorialStepsData.length - 1) {
                currentStep++;
                showTutorialStep(currentStep);
            } else {
                closeTutorial();
            }
        });
    }
    if (skipTutorialBtn) skipTutorialBtn.addEventListener('click', closeTutorial);
    if (helpBtn) helpBtn.addEventListener('click', startTutorial);

    const hasSeen = localStorage.getItem('trancit_tutorial_seen');
    if (!hasSeen) setTimeout(startTutorial, 1000);

    const tabPlan = $('#tabPlan');
    const tabSuggestions = $('#tabSuggestions');
    const panelSidebar = $('.sidebar');
    const panelSuggestions = $('.suggestions');

    if (tabPlan && tabSuggestions) {
        function handleTabSwitch(mode) {
            [tabPlan, tabSuggestions].forEach(t => t.classList.remove('active'));
            [panelSidebar, panelSuggestions].forEach(p => p.classList.remove('active-panel'));
            if (mode === 'plan') { tabPlan.classList.add('active'); panelSidebar.classList.add('active-panel'); }
            else { tabSuggestions.classList.add('active'); panelSuggestions.classList.add('active-panel'); }
        }
        tabPlan.addEventListener('click', () => handleTabSwitch('plan'));
        tabSuggestions.addEventListener('click', () => handleTabSwitch('suggestions'));
    }

    const panels = [panelSidebar, panelSuggestions];
    panels.forEach(panel => {
        const handle = panel ? panel.querySelector('.drag-handle') : null;
        if (!handle) return;
        let startY, startHeight;
        handle.addEventListener('touchstart', (e) => {
            startY = e.touches[0].clientY;
            startHeight = parseInt(document.defaultView.getComputedStyle(panel).height, 10);
            panel.classList.add('is-dragging'); 
        }, { passive: false });
        handle.addEventListener('touchmove', (e) => {
            if (!startY) return;
            e.preventDefault(); 
            const currentY = e.touches[0].clientY;
            const deltaY = startY - currentY; 
            const newH = startHeight + deltaY;
            if (newH > window.innerHeight * 0.20 && newH < window.innerHeight * 0.90) panel.style.height = `${newH}px`;
        }, { passive: false });
        handle.addEventListener('touchend', () => {
            panel.classList.remove('is-dragging');
            const h = parseInt(panel.style.height, 10);
            if (h > window.innerHeight * 0.70) panel.style.height = '85vh';
            else if (h < window.innerHeight * 0.30) panel.style.height = '25vh';
            else panel.style.height = '45vh';
            startY = null;
        });
        handle.addEventListener('mousedown', (e) => {
            startY = e.clientY;
            startHeight = parseInt(document.defaultView.getComputedStyle(panel).height, 10);
            panel.classList.add('is-dragging');
            const onMouseMove = (me) => {
                const delta = startY - me.clientY;
                const newH = startHeight + delta;
                if(newH > 100 && newH < window.innerHeight - 50) panel.style.height = `${newH}px`;
            };
            const onMouseUp = () => {
                panel.classList.remove('is-dragging');
                document.removeEventListener('mousemove', onMouseMove);
                document.removeEventListener('mouseup', onMouseUp);
            };
            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
        });
    });

    resetFormBtn?.addEventListener('click', () => window.location.href = '/routes/');
});