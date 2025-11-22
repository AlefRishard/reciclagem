function onEachFeature(feature, layer) {
	var popupContent = feature.properties.popup_content;
	layer.bindPopup(popupContent);
}


const gstreets = L.tileLayer('http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}', {
	maxZoom: 20, attribution: 'google'
});

const satellite = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
	maxZoom: 20, attribution: 'google'
});

const myStyle = {
	fillColor: 'white',
	weight: 2,
	opacity: 1,
	color: 'black',
	fillOpacity: 1,
	radius: 4,
}

const pontos = L.geoJson([], {
	pointToLayer: function (feature, latlng) {
		return new L.CircleMarker(latlng, myStyle);
	},
	onEachFeature: onEachFeature,
});

const pontos_url = $("#pontos_geojson").val();

$.getJSON(pontos_url, function (data) {
	pontos.addData(data);
});

const heat = L.heatLayer(pontosCoord, {
	radius: 22,
	blur: 30,
	minOpacity: 0.7,
})


const map = L.map('map', {
	center: [-3.0870395061289386, -59.98878479003907],
	zoom: 12,
	layers: [gstreets,
		 pontos,
		]
});


const baseLayers = {
	'Google Streets': gstreets,
	'Google Satélite': satellite
};

const overlays = {
	"Pontos": pontos,
};

const control = L.control.layers(baseLayers, overlays).addTo(map);

