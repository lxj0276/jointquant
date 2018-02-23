def pick_strategy_gross_profit():
    g.strategy_memo = '首席质量因子'
    buy_count = 3

    pick_config = [
        [True, '', '多因子范围选取器', Pick_financial_data, {
            'factors': [
                # FD_Factor('valuation.circulating_market_cap', min=0, max=100)  # 流通市值0~100亿
                FD_Factor('valuation.pe_ratio', min=0),  # pe > 0
                FD_Factor('valuation.pb_ratio', min=0),  # pb_ratio > 0
                FD_Factor('valuation.ps_ratio', max=2.5)
            ]
        }],
        [True, '', '多因子过滤器', Filter_financial_data, {
            'filters': [
                FD_Filter('valuation.market_cap',sort=SortType.desc, percent=80),
                FD_Filter('valuation.pe_ratio',sort=SortType.asc, percent=40),
                FD_Filter('valuation.pb_ratio',sort=SortType.asc, percent=40),

            ]
        }],
        [True, '', '过滤创业板', Filter_gem, {}],
        [True, '', '过滤ST,停牌,涨跌停股票', Filter_common, {}],
        [True, '', '权重排序', SortRules, {
            'config': [
                [True, '', '首席质量因子排序', Sort_gross_profit, {
                    'sort': SortType.desc,
                    'weight': 100}]
            ]}
        ],
        [True, '', '获取最终选股数', Filter_buy_count, {
            'buy_count': buy_count  # 最终入选股票数
        }],
    ]
    pick_new = [
        [True, '_pick_stocks_', '选股', Pick_stocks, {
            'config': pick_config,
            'day_only_run_one': True
        }]
    ]

    return pick_new