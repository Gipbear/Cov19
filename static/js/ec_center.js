let ec_center = echarts.init(document.getElementById(('c2')), "dark");
let my_data = [{'name': '上海', 'value': '318'}, {'name': '云南', 'value': '162'}];

let ec_center_option = {
    // backgroundColor: '#B2E0FF',  		// 图表背景色

    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    // 工具栏
    tooltip: {
        trigger: 'item'
    },
    // 左侧小导航图标，图例
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{start: 1, end: 9},
            {start: 10, end: 99},
            {start: 100, end: 999},
            {start: 1000, end: 9999},
            {start: 10000}],
        color: ['#8A3310', '#C64918', '#F55825', '#F2AD92', '#F9DCD1']
    },
    // 配置属性
    series: [{
        name: '累计确诊人数',
        type: 'map',
        mapType: 'china',
        roam: false, // 拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: 0.5, // 区域边框宽度
                borderColor: '#009FE8', // 区域边框颜色
                areaColor: '#FFEFD5', // 区域颜色
            },
            emphasis: { // 鼠标花朵地图高亮的相关设置
                borderWidth: 0.5, // 区域边框宽度
                borderColor: '#4B0082', // 区域边框颜色
                areaColor: '#FFFFFF', // 区域颜色
            }
        },
        label: {
            normal: {
                show: true, // 省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data: my_data // 数据
    }]
};
ec_center.setOption(ec_center_option)