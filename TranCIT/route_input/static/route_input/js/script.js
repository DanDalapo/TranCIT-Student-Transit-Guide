document.addEventListener('DOMContentLoaded', () => {
    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => document.querySelectorAll(sel);

    const routeForm = $('#routeForm');
    const originInput = $('#id_origin');
    const destinationInput = $('#id_destination');
    const suggestionsContainer = $('#destinationSuggestions');
    const transportSelect = $('#id_transport_type');
    const fareDisplay = $('#calculatedFare');
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

    const mapIframe = $('#map-container iframe');
    let foliumMap; 
    let L_Leaflet; 
    let activeRouteLayers = {}; 

    const csrftoken = document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1];

    // === Utilities ===
    const alertMsg = (msg) => alert(msg);
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
            if (mapIframe.contentWindow.map) {
                foliumMap = mapIframe.contentWindow.map;
            }
            if (mapIframe.contentWindow.L) {
                L_Leaflet = mapIframe.contentWindow.L;
            }
        }
        return foliumMap && L_Leaflet;
    }
    setTimeout(getMapObjects, 1500);

    function toggleNavigateButton() {
        const hasOrigin = originLat.value && originLon.value;
        const hasDestination = destLat.value && destLon.value;
        const enabled = hasOrigin && hasDestination;

        navigateBtn.disabled = !enabled;
        navigateBtn.style.opacity = enabled ? 1 : 0.6;
        navigateBtn.style.cursor = enabled ? 'pointer' : 'not-allowed';
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
    window.addEventListener('pageshow', syncInputsFromURL);

    const tooltip = document.createElement('div');
    tooltip.textContent = 'Please pin both your origin and destination';
    Object.assign(tooltip.style, {
        position: 'absolute',
        background: '#333',
        color: '#fff',
        padding: '6px 10px',
        borderRadius: '6px',
        fontSize: '12px',
        whiteSpace: 'nowrap',
        pointerEvents: 'none',
        opacity: '0',
        transition: 'opacity 0.2s'
    });
    document.body.appendChild(tooltip);

    const showTooltip = (e) => {
        if (!navigateBtn.disabled) return;
        tooltip.style.left = e.pageX + 15 + 'px';
        tooltip.style.top = e.pageY - 35 + 'px';
        tooltip.style.opacity = '1';
    };
    const hideTooltip = () => (tooltip.style.opacity = '0');
    navigateBtn?.addEventListener('mousemove', showTooltip);
    navigateBtn?.addEventListener('mouseleave', hideTooltip);

    const saveTooltip = document.createElement('div');
    saveTooltip.textContent = 'Please navigate a route first before saving';
    Object.assign(saveTooltip.style, {
        position: 'absolute',
        background: '#333',
        color: '#fff',
        padding: '6px 10px',
        borderRadius: '6px',
        fontSize: '12px',
        whiteSpace: 'nowrap',
        pointerEvents: 'none',
        opacity: '0',
        transition: 'opacity 0.2s'
    });
    document.body.appendChild(saveTooltip);

    const showSaveTooltip = (e) => {
        if (!saveMyRouteBtn.disabled) return;
        saveTooltip.style.left = e.pageX + 15 + 'px';
        saveTooltip.style.top = e.pageY - 35 + 'px';
        saveTooltip.style.opacity = '1';
    };
    const hideSaveTooltip = () => (saveTooltip.style.opacity = '0');
    saveMyRouteBtn?.addEventListener('mousemove', showSaveTooltip);
    saveMyRouteBtn?.addEventListener('mouseleave', hideSaveTooltip);

    function sendPinCommand(mode) {
        const iframe = document.querySelector('#map-container iframe');
        if (!iframe?.contentWindow) return alertMsg('Map not ready yet. Please wait.');

        const params = new URLSearchParams(window.location.search);
        if (mode === 'origin' && destLat.value && destLon.value) {
            params.set('destination_latitude', destLat.value);
            params.set('destination_longitude', destLon.value);
            params.set('destination_text', destinationInput.value);
        } else if (mode === 'destination' && originLat.value && originLon.value) {
            params.set('origin_latitude', originLat.value);
            params.set('origin_longitude', originLon.value);
            params.set('origin_text', originInput.value);
        }

        updateURL(params);
        iframe.contentWindow.postMessage({ type: 'SET_PIN_MODE', mode }, '*');
    }

    pinOriginBtn?.addEventListener('click', () => sendPinCommand('origin'));
    pinDestinationBtn?.addEventListener('click', () => sendPinCommand('destination'));

    navigateBtn?.addEventListener('click', () => {
        if (!originLat.value && !destLat.value) return alertMsg('Please pin both your origin and destination.');
        if (!originLat.value) return alertMsg('Please pin your origin.');
        if (!destLat.value) return alertMsg('Please pin your destination.');

        window.location.href = `/routes/?${qs({
            origin_latitude: originLat.value,
            origin_longitude: originLon.value,
            destination_latitude: destLat.value,
            destination_longitude: destLon.value,
            origin_text: originInput.value,
            destination_text: destinationInput.value,
            transport_type: transportSelect.value
        })}`;
    });

    function updateFare() {
        if (distInput && distInput.value && parseFloat(distInput.value) > 0) {
            return; 
        }
        const type = transportSelect?.value;
        if (!type) return;

        fareDisplay.textContent = 'Php 0.00';
        fareInput.value = '0.00';
        distInput.value = '';
        timeInput.value = '';

        if (type === 'Jeepney') {
            if (codeInput) codeInput.value = 'UNKNOWN';
            fareInput.value = '13.00';
            fareDisplay.textContent = 'Php ~13.00 (Fixed)';
            return;
        }

        if (!['Taxi', 'Motorcycle'].includes(type)) return;

        const dist = 5 + Math.random() * 10;
        const time = dist * 3;
        const fare = type === 'Taxi' ? 40 + 13.5 * dist + 2 * time : 20 + 10 * dist;

        distInput.value = dist.toFixed(2);
        timeInput.value = time.toFixed(2);
        fareInput.value = fare.toFixed(2);
        fareDisplay.textContent = `Php ${fare.toFixed(2)}`;
    }

    ['change', 'input'].forEach(evt => {
        transportSelect?.addEventListener(evt, updateFare);
        originInput?.addEventListener(evt, updateFare);
        destinationInput?.addEventListener(evt, updateFare);
    });
    updateFare();

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

                const params = {
                    origin_latitude: lat,
                    origin_longitude: lon,
                    origin_text: addr
                };
                if (destLat.value && destLon.value) {
                    params.destination_latitude = destLat.value;
                    params.destination_longitude = destLon.value;
                    params.destination_text = destinationInput.value;
                }
                window.location.href = `${window.location.pathname}?${qs(params)}`;
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
                const res = await fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}, Cebu City, Philippines&format=json&limit=5`);
                const results = await res.json();

                suggestionsContainer.innerHTML = '';
                if (!results.length) return (suggestionsContainer.style.display = 'none');

                results.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'destination-suggestions-item';
                    div.textContent = item.display_name;

                    div.addEventListener('click', () => {
                        destinationInput.value = item.display_name;
                        destLat.value = item.lat;
                        destLon.value = item.lon;
                        suggestionsContainer.style.display = 'none';
                        toggleNavigateButton();

                        const params = {
                            destination_latitude: item.lat,
                            destination_longitude: item.lon,
                            destination_text: item.display_name
                        };
                        if (originLat.value && originLon.value) {
                            params.origin_latitude = originLat.value;
                            params.origin_longitude = originLon.value;
                            params.origin_text = originInput.value;
                        }
                        window.location.href = `${window.location.pathname}?${qs(params)}`;
                    });
                    suggestionsContainer.appendChild(div);
                });
                suggestionsContainer.style.display = 'block';
            } catch {
                suggestionsContainer.style.display = 'none';
            }
        }, 400);
    });

    document.addEventListener('click', (e) => {
        if (!suggestionsContainer.contains(e.target) && e.target !== destinationInput)
            suggestionsContainer.style.display = 'none';
    });

    if (saveMyRouteBtn) {
        saveMyRouteBtn.addEventListener('click', () => {
            const formData = new FormData();
            formData.append('origin', $('#id_origin').value);
            formData.append('destination', $('#id_destination').value);
            formData.append('transport_type', $('#id_transport_type').value);
            formData.append('origin_latitude', $('#id_origin_latitude').value);
            formData.append('origin_longitude', $('#id_origin_longitude').value);
            formData.append('destination_latitude', $('#id_destination_latitude').value);
            formData.append('destination_longitude', $('#id_destination_longitude').value);
            formData.append('fare', $('#id_fare').value);
            formData.append('distance_km', $('#id_distance_km').value);
            formData.append('travel_time_minutes', $('#id_travel_time_minutes').value);
            formData.append('notes', $('#id_notes').value);
            
            if ($('#id_transport_type').value === 'Jeepney') {
                const codeInput = $('#suggest_code');
                if (codeInput && codeInput.value) {
                     formData.append('code', codeInput.value);
                } else {
                     formData.append('code', 'UNKNOWN');
                }
            }
            performSave('/routes/save_current_route/', formData);
        });
    }

    const saveSuggestionsContainer = $('#dynamicSuggestions');
    if (saveSuggestionsContainer) {
        saveSuggestionsContainer.addEventListener('click', (e) => {
            const saveButton = e.target.closest('.save-suggested-route');
            const viewButton = e.target.closest('.view-suggested-route');
            if (saveButton) {
                const routeId = saveButton.dataset.routeId;
                if (!routeId) return alert('Error: No route ID found.');
                const formData = new FormData();
                formData.append('route_id', routeId);
                performSave('/routes/save_suggested_route/', formData);
            }
            if (viewButton) { 
                handleViewRouteClick(viewButton);
            }
        });
    }

    function handleViewRouteClick(button) {
        if (!getMapObjects()) return alert('Map is not ready yet. Please wait a moment and try again.');

        const routeId = button.dataset.routeId;
        const isViewing = button.classList.contains('viewing');

        if (isViewing) {
            if (activeRouteLayers[routeId]) {
                foliumMap.removeLayer(activeRouteLayers[routeId]); 
                delete activeRouteLayers[routeId]; 
            }
            const originalText = button.classList.contains('view-saved-route') ? 'View' : 'View Route';
            button.innerHTML = `<i class="fa-solid fa-map"></i> ${originalText}`;
            button.classList.remove('viewing');
            button.style.backgroundColor = '#2196F3'; 
        } else {
            const ds = button.dataset; 
            if (!ds.path || ds.path.length < 3 || !ds.originLat || !ds.destLat) {
                alert('Error: No path data found for this route.');
                return;
            }

            try {
                const pathCoords = JSON.parse(ds.path);
                const originPopup = ds.routeOrigin || "Origin";
                const destPopup = ds.routeDestination || "Destination";

                const polyline = L_Leaflet.polyline(pathCoords, { color: 'purple', weight: 4, opacity: 0.8 });
                let originMarker, destMarker;

                try {
                    const originIcon = L_Leaflet.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'blue' });
                    const destIcon = L_Leaflet.AwesomeMarkers.icon({ icon: 'circle', prefix: 'fa', markerColor: 'red' });
                    originMarker = L_Leaflet.marker([ds.originLat, ds.originLon], {icon: originIcon}).bindPopup(originPopup);
                    destMarker = L_Leaflet.marker([ds.destLat, ds.destLon], {icon: destIcon}).bindPopup(destPopup);
                } catch (iconError) {
                    originMarker = L_Leaflet.marker([ds.originLat, ds.originLon]).bindPopup(originPopup);
                    destMarker = L_Leaflet.marker([ds.destLat, ds.destLon]).bindPopup(destPopup);
                }

                const routeLayerGroup = L_Leaflet.featureGroup([polyline, originMarker, destMarker]);
                routeLayerGroup.addTo(foliumMap);
                foliumMap.fitBounds(routeLayerGroup.getBounds().pad(0.1));
                activeRouteLayers[routeId] = routeLayerGroup;

                const unviewText = button.classList.contains('view-saved-route') ? 'Unview' : 'Unview Route';
                button.innerHTML = `<i class="fa-solid fa-eye-slash"></i> ${unviewText}`;
                button.classList.add('viewing');
                button.style.backgroundColor = '#f44336'; 
            } catch (err) {
                console.error('Error showing route:', err);
                alert('Error: Could not display this route.');
            }
        }
    }
    
    async function performSave(url, formData) {
        if (!csrftoken) return alert('Error: CSRF token not found.');
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' },
                body: formData
            });
            const data = await response.json();
            if (response.ok && data.message) {
                alert(data.message); 
                window.location.reload();
            } else {
                alert('Error saving route: ' + (data.error || 'Unknown error'));
            }
        } catch (error) {
            alert('An error occurred while trying to save the route.');
        }
    }

    const savedListContainer = $('#savedList');
    if (savedListContainer) {
        savedListContainer.addEventListener('click', (e) => {
            const deleteButton = e.target.closest('.delete-saved-route');
            const viewButton = e.target.closest('.view-saved-route');
            if (deleteButton) {
                const savedId = deleteButton.dataset.savedId;
                if (confirm('Are you sure you want to delete this route?')) {
                    const formData = new FormData();
                    formData.append('saved_id', savedId);
                    const elementToRemove = deleteButton.closest('.saved-route-item');
                    performDelete('/routes/delete_saved_route/', formData, elementToRemove);
                }
            }
            if (viewButton) handleViewRouteClick(viewButton); 
        });
    }

    async function performDelete(url, formData, elementToRemove) {
        if (!csrftoken) return alert('Error: CSRF token not found.');
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' },
                body: formData
            });
            const data = await response.json();
            if (response.ok && data.success) {
                elementToRemove.style.opacity = '0';
                setTimeout(() => { elementToRemove.remove(); }, 300);
            } else {
                alert('Error deleting route: ' + (data.error || 'Unknown error'));
            }
        } catch (error) {
            alert('An error occurred while trying to delete the route.');
        }
    }

    // MOBILE TAB SWITCHING LOGIC
    const tabPlan = $('#tabPlan');
    const tabSuggestions = $('#tabSuggestions');
    const panelSidebar = $('.sidebar');
    const panelSuggestions = $('.suggestions');

    if (tabPlan && tabSuggestions) {
        function handleTabSwitch(mode) {
            [tabPlan, tabSuggestions].forEach(t => t.classList.remove('active'));
            [panelSidebar, panelSuggestions].forEach(p => p.classList.remove('active-panel'));

            if (mode === 'plan') {
                tabPlan.classList.add('active');
                panelSidebar.classList.add('active-panel');
            } else {
                tabSuggestions.classList.add('active');
                panelSuggestions.classList.add('active-panel');
            }
        }
        tabPlan.addEventListener('click', () => handleTabSwitch('plan'));
        tabSuggestions.addEventListener('click', () => handleTabSwitch('suggestions'));
    }

    // DRAGGABLE BOTTOM SHEET LOGIC
    const panels = [panelSidebar, panelSuggestions];

    panels.forEach(panel => {
        const handle = panel.querySelector('.drag-handle');
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
            const newHeight = startHeight + deltaY;

            const minHeight = window.innerHeight * 0.20; 
            const maxHeight = window.innerHeight * 0.90; 

            if (newHeight > minHeight && newHeight < maxHeight) {
                panel.style.height = `${newHeight}px`;
            }
        }, { passive: false });

        handle.addEventListener('touchend', () => {
            panel.classList.remove('is-dragging');
            const currentHeight = parseInt(panel.style.height, 10);
            const screenHeight = window.innerHeight;

            if (currentHeight > screenHeight * 0.70) {
                panel.style.height = '85vh';
            } else if (currentHeight < screenHeight * 0.30) {
                panel.style.height = '25vh';
            } else {
                panel.style.height = '45vh';
            }
            startY = null;
        });
    });
});