var myDiagram;
var myModel;
function goJsInit()
{
    var myDiagramDiv = document.getElementById("myDiagramDiv");
    var parentDiv = document.getElementById("Diagram");
    parentDiv.removeChild(myDiagramDiv);
    var div = document.createElement('div');
    div.setAttribute('id', 'myDiagramDiv');
    div.setAttribute('style', 'width:100%;height:100%');
    parentDiv.appendChild(div);
	var $ = go.GraphObject.make;
	
	myDiagram = $(go.Diagram, "myDiagramDiv",
	{
		initialContentAlignment: go.Spot.TopCenter,
		allowMove: false,
		allowZoom: true,
		"undoManager.isEnabled": false,
		allowHorizontalScroll: true,
		allowVerticalScroll: false
		// autoScale:go.Diagram.Uniform
	});
	myDiagram.layout = $(go.TreeLayout, { angle: 90, layerSpacing: 70 });
	myDiagram.toolManager.toolTipDuration = 20000;
	
	// get tooltip text from the object's data
	function tooltipTextConverter(node) {
		var str = "";
		if (node.ip != undefined)
			str += node.ip;
		return str;
	}
	
	// define tooltips for nodes
	var tooltiptemplate =
		$("ToolTip",
			{ "Border.fill": "whitesmoke", "Border.stroke": "transparent"},
			$(go.TextBlock,
			{
				font: "10pt Segoe UI, sans-serif",
				wrap: go.TextBlock.WrapFit,
				margin: 5
			},
			new go.Binding("text", "", tooltipTextConverter))
	);

    var nodeContextMenu =
        $(go.Adornment, "Spot",
        { background: "transparent" },  // to help detect when the mouse leaves the area
        $(go.Placeholder),
        $(go.Panel, "Vertical",
            { alignment: go.Spot.Right, alignmentFocus: go.Spot.Left },
            $("Button",
            $(go.TextBlock, new go.Binding("text", "hostsInfo")),            
            /* {
                click: function(e, obj) {
                    var clicked = obj.part;

                    if (clicked !== null) {
                        var node = obj.part.adornedPart;                                        
                        var thisdata = clicked.data;
                        var url = 'http://' + thisdata.ip;	

                        node.removeAdornment("ContextMenuOver");
                        window.open(url);
                    }
                }
            } */
            )      
    ));

	myDiagram.nodeTemplate =
		$(go.Node, "Vertical",
		{ deletable: false, toolTip: tooltiptemplate },
		$(go.Picture, 
		{ margin: 10, width: 70, height: 70 },
			new go.Binding("source")
		),
		$(go.TextBlock,
		{ stroke: "black", font: "10pt Segoe UI, sans-serif" },
			new go.Binding("text", "key"),
			new go.Binding("background", "color")
		),
		$(go.TextBlock,
			{ stroke: "black", font: "10pt Segoe UI, sans-serif", alignment: go.Spot.Center},
				new go.Binding("text", "ip")
		),	
		$(go.TextBlock,
		{ stroke: "black", font: "10pt Segoe UI, sans-serif", alignment: go.Spot.Center},
			new go.Binding("text", "deviceName")
		),	
        {
            /* mouseEnter:function (e, node) {                
                var name =   node.data.name;              
                if (node.data.name != 'gateway') {
                    nodeContextMenu.adornedObject = node;
                    nodeContextMenu.mouseLeave = function (ev, cm) {
                        node.removeAdornment("ContextMenuOver");
                    }
                    node.addAdornment("ContextMenuOver", nodeContextMenu);   
                }
            } */
        }
	);

	myDiagram.linkTemplateMap.add(
		"SolidLine",
		$(go.Link,
			{ routing: go.Link.Orthogonal, corner: 5 },
			$(go.Shape, 
				new go.Binding('stroke', 'color'),
				{ stroke: 'black', strokeWidth: 2 }),
			$(go.TextBlock,
				new go.Binding("text","text"),
				{
					textAlign:"left",
					font:"9pt helvetica, arial, sans-serif",
					stroke:"#179b78",
					segmentIndex: -1,
					segmentOffset:new go.Point(-5  , 16)
					// segmentOrientation: go.Link.OrientUpright
				}
			)
		)
	);
	
	myDiagram.linkTemplateMap.add(
		"SolidLineDisconnect",
		$(go.Link,
			{ routing: go.Link.Orthogonal, corner: 5 },
			$(go.Shape, 
				new go.Binding('stroke', 'color'),
				{ stroke: 'black', strokeWidth: 2 }),
			$(go.Panel, "Auto",  // this whole Panel is a link label
				$(go.Shape, "XLine", { width:25, height:25, fill:null, strokeWidth:4, margin:4, stroke: "red" })
			)
		)
	);
	
	myDiagram.linkTemplateMap.add(
		"DottedLine",
		$(go.Link,
			{ routing: go.Link.Orthogonal, corner: 5 },
			$(go.Shape, 
				new go.Binding('stroke', 'color'),
				{ stroke: 'black', strokeWidth: 2, strokeDashArray: [5, 5]}
			),
			$(go.TextBlock,
				new go.Binding("text", "text"),
				{
					textAlign: "center",
					font: "14pt helvetica, arial, sans-serif",
					stroke: "blue",
					margin: 2,
					minSize: new go.Size(10, NaN),
					segmentOffset: new go.Point(0, -16),
					editable: false
			})
		)
	);
	
	myDiagram.linkTemplateMap.add(
		"DottedLineDisconnect",
		$(go.Link,
			{ routing: go.Link.Orthogonal, corner: 5 },
			$(go.Shape, 
				new go.Binding('stroke', 'color'),
				{ stroke: 'black', strokeWidth: 2, strokeDashArray: [5, 5]}
			),
			$(go.Panel, "Auto",  // this whole Panel is a link label
				$(go.Shape, "XLine", { width:25, height:25, fill:null, strokeWidth:4, margin:4, stroke: "red" })
			)
		)
	);

    myDiagram.addDiagramListener("ObjectSingleClicked", function(e)
	{
		var part = e.subject.part;
		if ((part.data.source.indexOf("subnet") != -1) &&
			(part.data.ip != undefined) &&
			(part.data.ip.length > 0))
		{
			window.open("http://"+part.data.ip); 
		}
    });    
	
	myModel = $(go.GraphLinksModel);
}
function goJsReInit()
{
	myDiagram = null; 
	goJsInit();
	myModel = new go.GraphLinksModel();
}

function drawTopo(data) {
    var node = {};
	var masterMAC,subMAC_l1,subMAC_l2,subMAC_l3;
	var bytes;

    goJsReInit();
    myModel = new go.GraphLinksModel();
    myDiagram.model = myModel;
	
	for (const key in data) {
		masterMAC = key;
		node["key"] = key.toUpperCase();
		node["ip"] = data[key].ip;
		node["name"] = "masterGateway";
		node["source"] = "./img/master.png";
		myModel.addNodeData(node);

		var mainDevLists = data[key].devList;
		for (const key in mainDevLists) {
			const element = mainDevLists[key];
			subMAC_l1 = key;
			if (element.subFttrDev) {
				//subgateway
				node = {};
				node["key"] = key.toUpperCase();
				node["ip"] = element.ip;
				node["source"] = "./img/subnet.png";
				node["if"] = element.topoIfname;
				if (element.hostname) {
					bytes = hexToBytes(element.hostname);
					node["deviceName"] = gbkToUtf8(bytes);	
				}
				myModel.addNodeData(node);
				myModel.addLinkData({"from": masterMAC.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});

				var sublists = mainDevLists[key].devList;
				for (const key in sublists) {
					const element = sublists[key];
					subMAC_l2 = key;
					if (element.subFttrDev) {
						//subgateway
						node = {};
						node["key"] = key.toUpperCase();
						node["ip"] = element.ip;
						node["source"] = "./img/subnet.png";
						node["if"] = element.topoIfname;
						if (element.hostname) {
							bytes = hexToBytes(element.hostname);
							node["deviceName"] = gbkToUtf8(bytes);	
						}
						myModel.addNodeData(node);
						myModel.addLinkData({"from": subMAC_l1.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});

						var sublists_l3 = sublists[key].devList;
						for (const key in sublists_l3) {
							const element = sublists_l3[key];
							subMAC_l3 = key;
							if (element.subFttrDev) {
								//subgateway
								node = {};
								node["key"] = key.toUpperCase();
								node["ip"] = element.ip;
								node["source"] = "./img/subnet.png";
								node["if"] = element.topoIfname;
								if (element.hostname) {
									bytes = hexToBytes(element.hostname);
									node["deviceName"] = gbkToUtf8(bytes);	
								}
								myModel.addNodeData(node);
								myModel.addLinkData({"from": subMAC_l2.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});
							} else {
								//terminal
								node = {};
								node["key"] = key.toUpperCase();
								node["source"] = "./img/devices.png";
								node["ip"] = element.ip;
								node["if"] = element.topoIfname;
								if (element.hostname) {
									bytes = hexToBytes(element.hostname);
									node["deviceName"] = gbkToUtf8(bytes);	
								}
								myModel.addNodeData(node);
								myModel.addLinkData({"from": subMAC_l2.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});
							}
						}						
					} else {
						//terminal
						node = {};
						node["key"] = key.toUpperCase();
						node["source"] = "./img/devices.png";
						node["ip"] = element.ip;
						node["if"] = element.topoIfname;
						if (element.hostname) {
							bytes = hexToBytes(element.hostname);
							node["deviceName"] = gbkToUtf8(bytes);	
						}
						myModel.addNodeData(node);
						myModel.addLinkData({"from": subMAC_l1.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});
					}
				}
			} else {
				//terminal
				node = {};
				node["key"] = key.toUpperCase();
				node["source"] = "./img/devices.png";
				node["ip"] = element.ip;
				node["if"] = element.topoIfname;
				if (element.hostname) {
					bytes = hexToBytes(element.hostname);
					node["deviceName"] = gbkToUtf8(bytes);	
				}
				myModel.addNodeData(node);
				myModel.addLinkData({"from": masterMAC.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});

				var sublists = element.devList;
				for (const key in sublists) {
					const element = sublists[key];
					subMAC_l2 = key;
					//terminal
					node = {};
					node["key"] = key.toUpperCase();
					node["source"] = "./img/devices.png";
					node["ip"] = element.ip;
					node["if"] = element.topoIfname;
					if (element.hostname) {
						bytes = hexToBytes(element.hostname);
						node["deviceName"] = gbkToUtf8(bytes);	
					}
					myModel.addNodeData(node);
					myModel.addLinkData({"from": subMAC_l1.toUpperCase(), "to": key.toUpperCase(), "category": "SolidLine", "text":node["if"]});
				}
			}
		}
	}
}
