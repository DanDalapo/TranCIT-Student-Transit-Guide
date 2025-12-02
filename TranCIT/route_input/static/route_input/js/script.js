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
    const alternativeRoutesContainer = $('#alternativeRoutesContainer');
    const alternativeRoutesList = $('#alternativeRoutesList');
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
    
    // --- MODIFICATION: Added selector for the new swap button --- //
    const swapLocationsBtn = $('#swapLocationsBtn');

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
    let currentViewedBtn = null; // Track active view button for suggestions

    const csrftoken = document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1];

    const alertMsg = (msg) => typeof showNotification === 'function' ? showNotification(msg) : alert(msg);
    
    const qs = (params) => new URLSearchParams(params).toString();

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

    // === Navigate Route Logic ===
    navigateBtn?.addEventListener('click', (e) => {
        e.preventDefault();

        if (!transportSelect.value) {
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

            // --- HANDLE JEEPNEY SUGGESTIONS ---
            if (data.alternatives && data.alternatives.length > 0) {
                alternativeRoutesList.innerHTML = ''; 
                currentViewedBtn = null; // Reset state

                data.alternatives.forEach((jeep, index) => {
                    const li = document.createElement('li');
                    li.style.cssText = "margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #e0e0e0;";
                    
                    const btnId = `btn-view-${index}`;
                    const walkText = jeep.walk_dist ? `Walk ${jeep.walk_dist}` : 'Walk';

                    let htmlContent = `
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                            <div style="display: flex; align-items: center; gap: 8px;">`;
                    
                    if (jeep.type === 'direct') {
                        htmlContent += `
                            <span style="font-weight: bold; background: #2e7d32; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px;">${jeep.code}</span>
                            <span style="font-weight: 600; color: #333; font-size: 13px;">Direct Route</span>`;
                    } else {
                         htmlContent += `
                            <div style="display:flex; gap:2px;">
                                <span style="font-weight: bold; background: #2e7d32; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px;">${jeep.code_1}</span>
                                <i class="fa-solid fa-arrow-right" style="font-size:10px; align-self:center; color:#888;"></i>
                                <span style="font-weight: bold; background: #ff9800; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px;">${jeep.code_2}</span>
                            </div>
                            <span style="font-weight: 600; color: #333; font-size: 13px;">1 Transfer</span>`;
                    }
                    
                    htmlContent += `</div></div>
                        <div style="font-size: 12px; color: #555; padding-left: 4px; border-left: 2px solid #4CAF50; margin-left: 4px; margin-bottom: 8px;">
                            <div><i class="fa-solid fa-person-walking"></i> ${walkText} to <strong>${jeep.board_at}</strong></div>`;
                            
                    if (jeep.type === 'transfer') {
                         htmlContent += `
                            <div style="margin-top:4px; color:#e65100;">
                                <i class="fa-solid fa-shuffle"></i> Transfer at <strong>${jeep.transfer_at}</strong>
                            </div>
                            <div style="margin-top:4px;">
                                <i class="fa-solid fa-bus"></i> Ride <strong>${jeep.code_2}</strong> to <strong>${jeep.alight_at}</strong>
                            </div>`;
                    } else {
                         htmlContent += `<div><i class="fa-solid fa-file-arrow-down"></i> Get off at <strong>${jeep.alight_at}</strong></div>`;
                    }

                    // Added TYPE="BUTTON" to prevent refresh
                    htmlContent += `</div>
                        <button id="${btnId}" type="button" class="btn btn-sm" style="width: 100%; background-color: #2196F3; color: white; margin-top: 5px;">
                            <i class="fa-solid fa-eye"></i> View Path
                        </button>
                    `;

                    li.innerHTML = htmlContent;
                    alternativeRoutesList.appendChild(li);

                    // Add Click Listener
                    const btn = li.querySelector(`#${btnId}`);
                    if (btn) {
                        btn.addEventListener('click', (e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            toggleJeepneyRoute(jeep, btn);
                        });
                    }
                });
                
                alternativeRoutesContainer.style.display = 'block';
            } else {
                alternativeRoutesContainer.style.display = 'none';
            }

            if (saveMyRouteBtn) saveMyRouteBtn.disabled = false;
        })
        .catch(err => {
            console.error(err);
            alertMsg(`Error: ${err.message}`);
        })
        .finally(() => {
            navigateBtn.disabled = false;
            navigateBtn.innerHTML = '<i class="fa-solid fa-route"></i> Navigate Route';
            document.body.style.cursor = 'default';
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
        // Also clear suggested layer if it exists
        if (window.activeRouteLayers && window.activeRouteLayers['suggestedJeepVisual']) {
            foliumMap.removeLayer(window.activeRouteLayers['suggestedJeepVisual']);
            delete window.activeRouteLayers['suggestedJeepVisual'];
        }
        if (currentViewedBtn) {
            currentViewedBtn.innerHTML = '<i class="fa-solid fa-eye"></i> View Path';
            currentViewedBtn.style.backgroundColor = '#2196F3';
            currentViewedBtn.classList.remove('is-viewing');
            currentViewedBtn = null;
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
        
        // Toggle OFF if clicking same button
        if (currentActiveButton === button) {
            clearCurrentRoute();
            return;
        }
        
        // Reset OLD button
        clearCurrentRoute();

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
            button.style.backgroundColor = '#f44336'; 
        } catch (err) {
            console.error(err);
            alertMsg('Error displaying route.');
        }
    }

    // === Toggle Suggestion Logic ===
    function toggleJeepneyRoute(jeep, btn) {
        const routeId = 'suggestedJeepVisual';
        
        if (btn.classList.contains('is-viewing')) {
            if (window.activeRouteLayers && window.activeRouteLayers[routeId]) {
                foliumMap.removeLayer(window.activeRouteLayers[routeId]);
                delete window.activeRouteLayers[routeId];
            }
            btn.innerHTML = '<i class="fa-solid fa-eye"></i> View Path';
            btn.style.backgroundColor = '#2196F3';
            btn.classList.remove('is-viewing');
            currentViewedBtn = null;
        } else {
            if (currentViewedBtn && currentViewedBtn !== btn) {
                currentViewedBtn.innerHTML = '<i class="fa-solid fa-eye"></i> View Path';
                currentViewedBtn.style.backgroundColor = '#2196F3';
                currentViewedBtn.classList.remove('is-viewing');
            }
            btn.innerHTML = '<i class="fa-solid fa-eye-slash"></i> Unview';
            btn.style.backgroundColor = '#f44336';
            btn.classList.add('is-viewing');
            currentViewedBtn = btn;

            visualizeJeepneyOption(jeep);
        }
    }

    async function visualizeJeepneyOption(jeep) {
        if (!getMapObjects()) return;
        
        const routeId = 'suggestedJeepVisual';
        // Ensure global object exists
        if (!window.activeRouteLayers) window.activeRouteLayers = {};

        if (window.activeRouteLayers[routeId]) {
            foliumMap.removeLayer(window.activeRouteLayers[routeId]);
            delete window.activeRouteLayers[routeId];
        }
        
        document.body.style.cursor = 'wait';

        try {
            const layers = [];

            // 1. Walk Line
            const walkRes = await fetch('/routes/get_segment_path/', {
                method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken},
                body: JSON.stringify({start: jeep.origin_coords, end: jeep.board_coords, mode: 'walking'})
            });
            const walkData = await walkRes.json();
            if(walkData.path_coords) layers.push(L_Leaflet.polyline(walkData.path_coords, {color: '#2196F3', weight: 5, dashArray: '10,10'}));

            if (jeep.type === 'direct') {
                 const rideRes = await fetch('/routes/get_segment_path/', {
                    method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken},
                    body: JSON.stringify({start: jeep.board_coords, end: jeep.alight_coords, mode: 'driving'})
                });
                const rideData = await rideRes.json();
                if(rideData.path_coords) layers.push(L_Leaflet.polyline(rideData.path_coords, {color: '#4CAF50', weight: 6}));
                
                layers.push(L_Leaflet.marker(jeep.board_coords).bindPopup(`<b>Board Here</b><br>${jeep.board_at}`));
                layers.push(L_Leaflet.marker(jeep.alight_coords).bindPopup(`<b>Get Off</b><br>${jeep.alight_at}`));

            } else if (jeep.type === 'transfer') {
                // Leg 1
                const r1 = await fetch('/routes/get_segment_path/', {
                    method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken},
                    body: JSON.stringify({start: jeep.board_coords, end: jeep.transfer_coords, mode: 'driving'})
                });
                const d1 = await r1.json();
                if(d1.path_coords) layers.push(L_Leaflet.polyline(d1.path_coords, {color: '#2e7d32', weight: 6}));

                // Leg 2
                const r2 = await fetch('/routes/get_segment_path/', {
                    method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken},
                    body: JSON.stringify({start: jeep.transfer_coords, end: jeep.alight_coords, mode: 'driving'})
                });
                const d2 = await r2.json();
                if(d2.path_coords) layers.push(L_Leaflet.polyline(d2.path_coords, {color: '#ff9800', weight: 6}));

                const transferIcon = L_Leaflet.divIcon({
                    className: 'custom-div-icon',
                    html: `<div style="background-color: #ff9800; width: 14px; height: 14px; border-radius: 50%; border: 2px solid white;"></div>`
                });

                layers.push(L_Leaflet.marker(jeep.board_coords).bindPopup(`<b>1. Ride ${jeep.code_1}</b>`));
                layers.push(L_Leaflet.marker(jeep.transfer_coords, {icon: transferIcon}).bindPopup(`<b>2. Transfer</b>`));
                layers.push(L_Leaflet.marker(jeep.alight_coords).bindPopup(`<b>3. Get Off</b>`));
            }

            const group = L_Leaflet.featureGroup(layers);
            group.addTo(foliumMap);
            foliumMap.fitBounds(group.getBounds().pad(0.2));
            window.activeRouteLayers[routeId] = group;

        } catch (err) {
            console.error(err);
        } finally {
            document.body.style.cursor = 'default';
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

    // === Fare Estimation ===
    function updateFare() {
        if (distInput && distInput.value && parseFloat(distInput.value) > 0) return; 
        const type = transportSelect?.value;
        if (!type) return;

        calculatedFareEl.textContent = 'Php 0.00';
        calculatedTimeEl.textContent = '-- min';
        calculatedDistanceEl.textContent = '-- km';
        calculatedTransportEl.textContent = '--';
        fareInput.value = '0.00';
        distInput.value = '';
        timeInput.value = '';

        if (!originInput.value.trim() || !destinationInput.value.trim()) return;

        if (type === 'Jeepney') {
            if (codeInput) codeInput.value = 'UNKNOWN';
            fareInput.value = '13.00';
            calculatedFareEl.textContent = 'Php ~13.00 (Fixed)';
            calculatedTransportEl.textContent = 'Jeepney';
            return;
        }
    }
    
    ['change', 'input'].forEach(evt => {
        transportSelect?.addEventListener(evt, updateFare);
    });

    // === Tutorial Logic ===
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

    // === Geolocation Detection (FIXED) ===
    detectBtn?.addEventListener('click', () => {
        if (!navigator.geolocation) return alertMsg('Geolocation not supported.');
        originInput.value = 'Detecting location...';

        navigator.geolocation.getCurrentPosition(async pos => {
            const { latitude: lat, longitude: lon } = pos.coords;
            originLat.value = lat;
            originLon.value = lon;
            toggleNavigateButton();

            try {
                const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lon}`);
                const data = await res.json();
                const addr = data?.display_name || `Lat: ${lat.toFixed(5)}, Lon: ${lon.toFixed(5)}`;
                originInput.value = addr;

                // --- ADDED: Send PIN Command to Map ---
                if (mapIframe && mapIframe.contentWindow) {
                    mapIframe.contentWindow.postMessage({
                        type: 'DRAW_PIN',
                        mode: 'origin',
                        lat: lat,
                        lng: lon,
                        label: addr
                    }, '*');
                }

            } catch {
                alertMsg('Unable to retrieve address, but location saved.');
            }
        }, err => {
            console.error(err);
            alertMsg('Location detection failed.');
        }, { enableHighAccuracy: true, timeout: 7000 });
    });

    let debounce;
    destinationInput?.addEventListener('input', () => {
        clearTimeout(debounce);
        const query = destinationInput.value.trim();
        if (query.length < 3) return (suggestionsContainer.style.display = 'none');

        debounce = setTimeout(async () => {
            try {
                const viewbox = '123.70,10.55,124.10,10.10';
                const url = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}&format=json&limit=5&viewbox=${viewbox}&bounded=1&countrycodes=ph`;
                const res = await fetch(url);
                const results = await res.json();

                suggestionsContainer.innerHTML = '';
                if (!results.length) {
                    suggestionsContainer.innerHTML = '<div class="destination-suggestions-item">No results found</div>';
                    return;
                }

                results.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'destination-suggestions-item';
                    const cleanName = item.display_name.replace(', Central Visayas, Philippines', '').replace(', Philippines', '');
                    div.textContent = cleanName;

                    div.addEventListener('click', () => {
                        destinationInput.value = cleanName;
                        destLat.value = item.lat;
                        destLon.value = item.lon;
                        suggestionsContainer.style.display = 'none';
                        toggleNavigateButton();

                        if (mapIframe && mapIframe.contentWindow) {
                            mapIframe.contentWindow.postMessage({
                                type: 'DRAW_PIN', mode: 'destination', lat: item.lat, lng: item.lon, label: cleanName
                            }, '*');
                        }
                    });
                    suggestionsContainer.appendChild(div);
                });
                suggestionsContainer.style.display = 'block';
            } catch (error) {
                console.error("Search error:", error);
            }
        }, 400);
    });

    document.addEventListener('click', (e) => {
        if (!suggestionsContainer.contains(e.target) && e.target !== destinationInput)
            suggestionsContainer.style.display = 'none';
    });

    // --- MODIFICATION: Rewritten Reset Logic --- //
    resetFormBtn?.addEventListener('click', () => {
        // 1. Clear form inputs
        routeForm.reset();
        originLat.value = '';
        originLon.value = '';
        destLat.value = '';
        destLon.value = '';

        // 2. Reset the results display
        calculatedFareEl.textContent = 'Php 0.00';
        calculatedTimeEl.textContent = '-- min';
        calculatedDistanceEl.textContent = '-- km';
        calculatedTransportEl.textContent = '--';

        // 3. Hide alternative routes
        alternativeRoutesContainer.style.display = 'none';
        alternativeRoutesList.innerHTML = '';
        
        // 4. Clear any routes on the map
        clearCurrentRoute();
        if (getMapObjects()) {
            mapIframe.contentWindow.postMessage({ type: 'CLEAR_PINS' }, '*');
        }

        // 5. Disable buttons
        toggleNavigateButton();
        if (saveMyRouteBtn) saveMyRouteBtn.disabled = true;

        // 6. Clear URL parameters
        window.history.replaceState({}, '', window.location.pathname);
    });
    
    // --- MODIFICATION: Added Swap Logic --- //
    swapLocationsBtn?.addEventListener('click', () => {
        // Swap text values
        const tempOriginText = originInput.value;
        originInput.value = destinationInput.value;
        destinationInput.value = tempOriginText;

        // Swap latitude values
        const tempOriginLat = originLat.value;
        originLat.value = destLat.value;
        destLat.value = tempOriginLat;

        // Swap longitude values
        const tempOriginLon = originLon.value;
        originLon.value = destLon.value;
        destLon.value = tempOriginLon;
        
        // Update map pins if map is ready
        if (getMapObjects()) {
            // Clear old pins first
            mapIframe.contentWindow.postMessage({ type: 'CLEAR_PINS' }, '*');

            // Draw new pins
            if (originLat.value && originLon.value) {
                mapIframe.contentWindow.postMessage({
                    type: 'DRAW_PIN', mode: 'origin', lat: originLat.value, lng: originLon.value, label: originInput.value
                }, '*');
            }
            if (destLat.value && destLon.value) {
                mapIframe.contentWindow.postMessage({
                    type: 'DRAW_PIN', mode: 'destination', lat: destLat.value, lng: destLon.value, label: destinationInput.value
                }, '*');
            }
        }
    });

    if (saveMyRouteBtn) {
        saveMyRouteBtn.addEventListener('click', () => {
            const formData = new FormData(routeForm);
            performSave('/routes/save_current_route/', formData);
        });
    }
});