$(document).ready(function () {
	//Segundo  Rango de gravedad
	var theme = {
		color: [
			'#26B99A', '#34495E', '#BDC3C7', '#3498DB',
			'#9B59B6', '#8abb6f', '#759c6a', '#bfd3b7'
		],

		title: {
			itemGap: 8,
			textStyle: {
				fontWeight: 'normal',
				color: '#408829'
			}
		},

		dataRange: {
			color: ['#1f610a', '#97b58d']
		},

		toolbox: {
			color: ['#408829', '#408829', '#408829', '#408829']
		},

		tooltip: {
			backgroundColor: 'rgba(0,0,0,0.5)',
			axisPointer: {
				type: 'line',
				lineStyle: {
					color: '#408829',
					type: 'dashed'
				},
				crossStyle: {
					color: '#408829'
				},
				shadowStyle: {
					color: 'rgba(200,200,200,0.3)'
				}
			}
		},

		dataZoom: {
			dataBackgroundColor: '#eee',
			fillerColor: 'rgba(64,136,41,0.2)',
			handleColor: '#408829'
		},
		grid: {
			borderWidth: 0
		},

		categoryAxis: {
			axisLine: {
				lineStyle: {
					color: '#408829'
				}
			},
			splitLine: {
				lineStyle: {
					color: ['#eee']
				}
			}
		},

		valueAxis: {
			axisLine: {
				lineStyle: {
					color: '#408829'
				}
			},
			splitArea: {
				show: true,
				areaStyle: {
					color: ['rgba(250,250,250,0.1)', 'rgba(200,200,200,0.1)']
				}
			},
			splitLine: {
				lineStyle: {
					color: ['#eee']
				}
			}
		},
		timeline: {
			lineStyle: {
				color: '#408829'
			},
			controlStyle: {
				normal: { color: '#408829' },
				emphasis: { color: '#408829' }
			}
		},

		k: {
			itemStyle: {
				normal: {
					color: '#68a54a',
					color0: '#a9cba2',
					lineStyle: {
						width: 1,
						color: '#408829',
						color0: '#86b379'
					}
				}
			}
		},
		map: {
			itemStyle: {
				normal: {
					areaStyle: {
						color: '#ddd'
					},
					label: {
						textStyle: {
							color: '#c12e34'
						}
					}
				},
				emphasis: {
					areaStyle: {
						color: '#99d2dd'
					},
					label: {
						textStyle: {
							color: '#c12e34'
						}
					}
				}
			}
		},
		force: {
			itemStyle: {
				normal: {
					linkStyle: {
						strokeColor: '#408829'
					}
				}
			}
		},
		chord: {
			padding: 4,
			itemStyle: {
				normal: {
					lineStyle: {
						width: 1,
						color: 'rgba(128, 128, 128, 0.5)'
					},
					chordStyle: {
						lineStyle: {
							width: 1,
							color: 'rgba(128, 128, 128, 0.5)'
						}
					}
				},
				emphasis: {
					lineStyle: {
						width: 1,
						color: 'rgba(128, 128, 128, 0.5)'
					},
					chordStyle: {
						lineStyle: {
							width: 1,
							color: 'rgba(128, 128, 128, 0.5)'
						}
					}
				}
			}
		},
		gauge: {
			startAngle: 225,
			endAngle: -45,
			axisLine: {
				show: true,
				lineStyle: {
					color: [[0.2, '#86b379'], [0.8, '#68a54a'], [1, '#408829']],
					width: 8
				}
			},
			axisTick: {
				splitNumber: 10,
				length: 12,
				lineStyle: {
					color: 'auto'
				}
			},
			axisLabel: {
				textStyle: {
					color: 'auto'
				}
			},
			splitLine: {
				length: 18,
				lineStyle: {
					color: 'auto'
				}
			},
			pointer: {
				length: '90%',
				color: 'auto'
			},
			title: {
				textStyle: {
					color: '#333'
				}
			},
			detail: {
				textStyle: {
					color: 'auto'
				}
			}
		},
		textStyle: {
			fontFamily: 'Arial, Verdana, sans-serif'
		}
	};


	var echartGaugeRango = echarts.init(document.getElementById("echart_gauge_rango"), theme);
	// Solo tienes que mandar el nuevo valor
	var x = 25;
	var y = 55;
	var z = 20;



	echartGaugeRango.setOption({
		tooltip: {
			formatter: "{a} <br/>{b} : {c}%"
		},
		toolbox: {
			show: true,
			feature: {
				restore: {
					show: true,
					title: "Restore"
				},
				saveAsImage: {
					show: true,
					title: "Save Image"
				}
			}
		},
		series: [{
			name: 'Gravedad',
			type: 'gauge',
			center: ['50%', '50%'],
			startAngle: 140,
			endAngle: -140,
			min: 0,
			max: 100,
			precision: 0,
			splitNumber: 10,
			axisLine: {
				show: true,
				lineStyle: {
					color: [
						[0.3, 'lightgreen'],
						[0.7, 'skyblue'],
						[1, '#ff4500']
					],
					width: 30
				}
			},
			axisTick: {
				show: true,
				splitNumber: 5,
				length: 8,
				lineStyle: {
					color: '#eee',
					width: 1,
					type: 'solid'
				}
			},
			splitLine: {
				show: true,
				length: 30,
				lineStyle: {
					color: '#eee',
					width: 2,
					type: 'solid'
				}
			},
			pointer: {
				length: '80%',
				width: 8,
				color: 'auto'
			},
			title: {
				show: true,
				offsetCenter: ['-65%', -10],
				textStyle: {
					color: '#333',
					fontSize: 15
				}
			},
			detail: {
				show: true,
				backgroundColor: 'rgba(0,0,0,0)',
				borderWidth: 0,
				borderColor: '#ccc',
				width: 100,
				height: 40,
				offsetCenter: ['-60%', 10],
				formatter: '{value}%',
				textStyle: {
					color: 'auto',
					fontSize: 30
				}
			},
			data: [{
				value: z,
				name: 'Grave'
			},{
				value: y,
				name: 'Moderado'
			},{
				value: x,
				name: 'Leve'
			}]
		}]
	});

	// another
	var echartDonutRango = echarts.init(document.getElementById('echart_donut_rango'), theme);
			  
	echartDonutRango.setOption({
	  tooltip: {
		trigger: 'item',
		formatter: "{a} <br/>{b} : {c} ({d}%)"
	  },
	  calculable: true,
	  legend: {
		x: 'center',
		y: 'bottom',
		data: ['valor I', 'valor A', 'valor D', 'suma G', ]
	  },
	  toolbox: {
		show: true,
		feature: {
		  magicType: {
			show: true,
			type: ['pie', 'funnel'],
			option: {
			  funnel: {
				x: '25%',
				width: '50%',
				funnelAlign: 'center',
				max: 1548
			  }
			}
		  },
		  restore: {
			show: true,
			title: "Restore"
		  },
		  saveAsImage: {
			show: true,
			title: "Save Image"
		  }
		}
	  },
	  series: [{
		name: 'Factor violencia',
		type: 'pie',
		radius: ['35%', '55%'],
		itemStyle: {
		  normal: {
			label: {
			  show: true
			},
			labelLine: {
			  show: true
			}
		  },
		  emphasis: {
			label: {
			  show: true,
			  position: 'center',
			  textStyle: {
				fontSize: '14',
				fontWeight: 'normal'
			  }
			}
		  }
		},
		data: [{
		  value: 335,
			name: 'valor i'
		}, {
		  value: 310,
		  name: 'valor a '
		}, {
		  value: 80,
		  name: 'valor d'
		}, {
		  value: 150,
		  name: 'suma g'
		}]
	  }]
	});




});


