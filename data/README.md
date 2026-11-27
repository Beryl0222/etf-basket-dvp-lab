# 数据说明

所有数据均为合成资料。每张表的首行为字段名。

申请此前已收到的适用清单才可提交。optional 只在该证券不能按正常交割取得或处置、且选择了现金时启用。每篮替代预留额按数量乘参考价乘（1 加预留增幅），“按日”按受理日计算，确认退补前持续计入同日限额。申购属应收证券或预留款和应交份额，赎回方向反转。基金公布在本地演练中不包含额外基础现金差。替代证券成交各方向分别按已受理且已取得对应预留的时间顺位分配到申请，未达资格的申请延后，费用按单笔实际成交中各份额比例、四舍五入到分，尾差留给该成交末笔。文件保留所有回报的外部身份，收到未知或金额超合同的回报保留为待核事件。托管 principal 回执是篮子的证券、初始现金预留款或基金份额交付，cash_difference 是补付或退回的差额，return 是撤回后已交资产的退回。三个用途的 in、out 均按资金流向解释。撤回只在尚未完成篮子交收且还没有归该笔的替代成交时允许。已到托管的替代预留款在差额结清前仍归原单，不能视为基金的自由现金。申购的采购总成本包括费用，赎回的处置所得扣除费用。赎回预留款高于净处置所得时参与商退回差额，低于时由基金补付。

## baskets

- `revision` 篮子版
- `fund` 基金
- `day` 交易日
- `known` 发布时间 UTC
- `shares` 每篮份额
- `asset` 组成证券
- `units` 每篮证券数
- `create_rule` in_kind、optional 或 cash
- `redeem_rule` 同上
- `ref_price` 参考单价
- `premium` 替代预留增幅

## orders

- `order` 申请号
- `agent` 参与商
- `time` UTC 收件
- `side` create 或 redeem
- `revision` 参与商认领版
- `baskets` 篮数
- `requested_cash` 主动要求替代的证券，竖线分隔

## vault_open

- `owner` 托管账户
- `asset` 基金份额、证券或 CASH
- `units` 到账可用数量

## venue_restrictions

- `day` 交易日
- `fund` 基金
- `asset` 证券或 ALL
- `at` UTC 生效
- `can_trade` 市场能否取得或处置
- `per_order_cash` 单个申请替代金额上限
- `fund_cash` 基金日内替代金额上限

## custody

- `id` 回执号
- `order` 申请
- `asset` 资产
- `direction` in 为参与商付基金，out 反向
- `status` confirmed 或 rejected
- `qty` 交付量
- `at` UTC 到达
- `purpose` principal 为初始交付，cash_difference 为退补差额，return 为原交付退回

## cancellations

- `id` 参与商撤回身份
- `order` 原申请号
- `agent` 撤回方，需与原申请相符
- `at` 撤回 UTC 时点

## hedge_fills

- `fill` 实际采购或处置成交
- `fund` 基金
- `asset` 组成证券
- `side` buy 或 sell
- `qty` 成交股数
- `price` 单价
- `fee` 该笔总费用
- `at` UTC 成交
