# 融合依据与证据边界

本包采用原创调度说明，引用已有技能按需调用，不复制或捆绑第三方仓库、模型权重和密钥。创建时点：2026-09-05。外部资料为厂商/作者声明，未以本包实际生成动画验证。

| 来源 | 吸收的优点 | 具体融合与修正 |
|---|---|---|
| 总经理 | CEO只定目标，执行方负责选择；独立审计、证据晋级 | 普通参数自动补齐，最终审片与制作分开，保留在途成本和恢复状态 |
| novel-outline / characters / art / script / storyboard | 故事结构、稳定资产、节拍对白、关键帧和确定性校验 | 分离创作与模型提示词；长剧才用完整连载门；单集动画有独立路线 |
| ChatCut 视频、声音、剪辑与导出技能 | 工程内资产和多模型生产、时间线编辑 | 明确生成资产之后还需排片、对声音、预览、导出；异步真实续接 |
| Higgsfield | 自然语言规划、连续分镜、角色身份、导演参数 | 用于创意补齐和按镜头编译，不把营销功能当本机可用 API |
| LTX Studio | 角色/地点/物体复用、关键帧、镜头级返工 | 统一资产版本与上下游依赖，改角色时定位所有相关镜头 |
| StoryMind | 导演式镜头表、情绪转摄影指令、后期组合 | 用可见动作和摄影语法表达情绪；原仓库实现仍需独立审查 |
| ai-video-pipeline | 先角色与分镜、后运动、再合成；逐任务记录 | 小样先验证、局部重做、产物可追溯，不采信“完全解决一致性”保证 |
| Tencent/MimicMotion | 置信度姿态引导、姿态序列驱动、时间连续性 | 只作为姿态迁移候选；不把人体姿态模型当成非人形角色 rig，也不把仓库结果当本机实测 |
| guoyww/AnimateDiff + ControlNet/SparseCtrl | 用视频、OpenPose、草图或稀疏控制图约束动画 | 作为风格化/姿态条件路线；保留闪烁、空间接触和显存限制，不能替代逐招动作表 |
| htdt/kimodo-practical / NVIDIA Kimodo 方法 | canonical skeleton、根运动、手脚末端目标、路径、IK、rig 认证、QA gate | 将“先认证角色、再生成动作、最后烘焙”写成动作片硬门；对奶龙等非人形角色必须先建立代理/rig 映射 |

外部参考：

- https://higgsfield.ai/supercomputer-intro
- https://higgsfield.ai/blog/script-to-ai-storyboard-shot-list
- https://ltx.io/studio/platform/ai-movie-maker
- https://www.minimax.io/news/minimax-h3-open-source
- https://github.com/LinHao-city/StoryMind
- https://github.com/0xadvait/ai-video-pipeline
- https://github.com/Tencent/MimicMotion
- https://github.com/guoyww/AnimateDiff
- https://github.com/htdt/kimodo-practical

本包交付状态：组合规则已编写；结构验证、独立推演在包外留证；没有真实端到端成片证据。安装不自动开通工具权限或会员。未来升级由实际成片的问题与复盘驱动，不能把厂家宣称或规则审核当生产实测。
