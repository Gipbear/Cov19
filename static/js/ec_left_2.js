let ec_left2 = echarts.init(document.getElementById('l2'), 'dark')

let ec_left2_option = {
    //标题样式
    title: {
        text: '全国新增趋势图',
        textStyle: {
            // color:'white
        },
        left: 'left',
    },
    // 鼠标停留提示框
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: '#7171c6'
            }
        },
    },
    // 图例
    legend: {
        data: ['新增确诊', '新增疑似'],
        left: 'right',
    },
    // 图表距边框的距离
    grid: {
        left: '4%',
        right: '6%',
        bottom: '4%',
        top: 50,
        containLabel: true
    },
    // 工具框，可以选择
    // toolbox: {
    //     feature: {
    //         saveAsImage: {} //下载工具
    //     }
    // },
    xAxis: {
        type: 'category',
        // x轴坐标点开始与结束点位置都不在最边缘
        // boundaryGap: true,
        data: []
    },
    yAxis: {
        type: 'value',
        // y轴字体设置
        axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
            formatter: function (value) {
                if (value >= 1000) {
                    value = value / 1000 + 'k';
                }
                return value;
            }
        },
        // y轴线设置显示
        axisLine: {
            show: true,
        },
        // 与x轴平行的线样式
        splitLine: {
            show: true,
            lineStyle: {
                color: '#172738',
                width: 1,
                type: 'solid',
            },
        },
    },
    series: [
        {
            name: '新增确诊',
            type: 'line',
            smooth: true,
            data: [],
        }, {
            name: '新增疑似',
            type: 'line',
            smooth: true,
            data: [],
        },
    ]
};

ec_left2.setOption(ec_left2_option)