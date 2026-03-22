#!/usr/bin/env python3
"""
孙子兵法战略分析器
基于五事七计框架，提供商业战略分析支持
"""

import json
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class StrategyLevel(Enum):
    """战略层级 - 从优到劣"""
    FA_MO = "上兵伐谋"      # 智慧取胜
    FA_JIAO = "其次伐交"    # 联盟取胜
    FA_BING = "其次伐兵"    # 正面对抗
    GONG_CHENG = "其下攻城" # 消耗战

@dataclass
class WuShi:
    """五事模型"""
    dao: str = ""    # 道 - 企业文化/使命愿景
    tian: str = ""   # 天 - 市场趋势/时机
    di: str = ""     # 地 - 行业格局/竞争态势
    jiang: str = ""  # 将 - 领导力/核心团队
    fa: str = ""     # 法 - 管理制度/执行体系

@dataclass
class QiJi:
    """七计对比"""
    zhu_dao: str = ""      # 主孰有道
    jiang_neng: str = ""   # 将孰有能
    tian_di: str = ""      # 天地孰得
    fa_ling: str = ""      # 法令孰行
    bing_zhong: str = ""   # 兵众孰强
    shi_zu: str = ""       # 士卒孰练
    shang_fa: str = ""     # 赏罚孰明

@dataclass
class Situation:
    """形势分析"""
    my_strengths: List[str]      # 我方优势
    my_weaknesses: List[str]     # 我方劣势
    opp_strengths: List[str]     # 对方优势
    opp_weaknesses: List[str]    # 对方劣势
    opportunities: List[str]     # 机会
    threats: List[str]           # 威胁

class SunZiAnalyzer:
    """孙子兵法商业分析器"""
    
    def __init__(self):
        self.wushi = WuShi()
        self.qiji = QiJi()
        self.situation = Situation([], [], [], [], [], [])
    
    def analyze_wushi(self, dao: str, tian: str, di: str, jiang: str, fa: str) -> Dict:
        """分析五事"""
        self.wushi = WuShi(dao, tian, di, jiang, fa)
        
        scores = {
            "道": self._score_element(dao),
            "天": self._score_element(tian),
            "地": self._score_element(di),
            "将": self._score_element(jiang),
            "法": self._score_element(fa)
        }
        
        total = sum(scores.values()) / 5
        
        return {
            "五事评分": scores,
            "综合评分": round(total, 1),
            "建议": self._get_wushi_advice(scores)
        }
    
    def analyze_qiji(self, comparisons: Dict[str, str]) -> Dict:
        """分析七计 - 与竞争对手对比"""
        result = {}
        advantage_count = 0
        
        for key, comparison in comparisons.items():
            if "我" in comparison or "优势" in comparison or "胜" in comparison:
                advantage_count += 1
                result[key] = "我方优势"
            elif "对方" in comparison or "劣势" in comparison or "负" in comparison:
                result[key] = "对方优势"
            else:
                result[key] = "势均力敌"
        
        win_rate = advantage_count / 7 * 100
        
        return {
            "七计分析": result,
            "优势项": advantage_count,
            "胜率": f"{win_rate:.0f}%",
            "建议": self._get_qiji_advice(win_rate)
        }
    
    def analyze_situation(self, my_strengths: List, my_weaknesses: List,
                         opp_strengths: List, opp_weaknesses: List,
                         opportunities: List, threats: List) -> Dict:
        """知彼知己分析"""
        self.situation = Situation(my_strengths, my_weaknesses, 
                                   opp_strengths, opp_weaknesses,
                                   opportunities, threats)
        
        # 判断虚实
        xu_shi = self._analyze_xu_shi()
        
        # 推荐战略
        strategy = self._recommend_strategy()
        
        return {
            "我方实力": {
                "实（优势）": my_strengths,
                "虚（劣势）": my_weaknesses
            },
            "对方实力": {
                "实（优势）": opp_strengths,
                "虚（劣势）": opp_weaknesses
            },
            "虚实判断": xu_shi,
            "推荐战略": strategy
        }
    
    def _score_element(self, element: str) -> int:
        """评分1-10"""
        if not element or element == "未知":
            return 5
        # 简单评分逻辑，实际应用可扩展
        if any(word in element for word in ["强", "优", "好", "领先"]):
            return 8
        elif any(word in element for word in ["弱", "劣", "差", "落后"]):
            return 4
        else:
            return 6
    
    def _get_wushi_advice(self, scores: Dict) -> List[str]:
        """五事改进建议"""
        advice = []
        for element, score in scores.items():
            if score < 5:
                if element == "道":
                    advice.append("加强企业文化建设，提升团队凝聚力")
                elif element == "天":
                    advice.append("深入研究市场趋势，把握时机")
                elif element == "地":
                    advice.append("优化市场定位，建立竞争壁垒")
                elif element == "将":
                    advice.append("强化领导团队，培养核心人才")
                elif element == "法":
                    advice.append("完善管理制度，提升执行力")
        return advice if advice else ["五事均衡，继续保持"]
    
    def _get_qiji_advice(self, win_rate: float) -> str:
        """七计建议"""
        if win_rate >= 70:
            return "优势明显，可主动出击，争取速胜"
        elif win_rate >= 50:
            return "势均力敌，应避实击虚，寻找破绽"
        else:
            return "劣势明显，应保存实力，等待时机"
    
    def _analyze_xu_shi(self) -> Dict:
        """分析虚实"""
        return {
            "我方之实": self.situation.my_strengths,
            "我方之虚": self.situation.my_weaknesses,
            "对方之实": self.situation.opp_strengths,
            "对方之虚": self.situation.opp_weaknesses,
            "攻击方向": f"避{self.situation.opp_strengths[0] if self.situation.opp_strengths else '未知'}，击{self.situation.opp_weaknesses[0] if self.situation.opp_weaknesses else '未知'}"
        }
    
    def _recommend_strategy(self) -> Dict:
        """推荐战略"""
        my_strength = len(self.situation.my_strengths)
        my_weakness = len(self.situation.my_weaknesses)
        opp_weakness = len(self.situation.opp_weaknesses)
        
        if my_strength >= 3 and opp_weakness >= 2:
            return {
                "层级": "伐谋/伐交",
                "策略": "上兵伐谋，不战而屈人之兵",
                "行动": "利用优势，通过战略定位、品牌塑造、联盟合作取得胜利"
            }
        elif my_strength >= 2:
            return {
                "层级": "伐兵",
                "策略": "避实击虚，集中优势兵力",
                "行动": "避开对手强项，攻击其薄弱环节"
            }
        else:
            return {
                "层级": "守势",
                "策略": "先为不可胜，以待敌之可胜",
                "行动": "保存实力，加强自身建设，等待对手犯错"
            }


def main():
    """示例使用"""
    analyzer = SunZiAnalyzer()
    
    # 五事分析示例
    print("=" * 50)
    print("【五事分析】")
    print("=" * 50)
    result = analyzer.analyze_wushi(
        dao="团队凝聚力强，使命愿景清晰",
        tian="市场处于增长期，政策利好",
        di="竞争激烈，需要差异化定位",
        jiang="核心团队经验丰富",
        fa="管理制度完善，执行力强"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 七计分析示例
    print("\n" + "=" * 50)
    print("【七计分析】")
    print("=" * 50)
    result = analyzer.analyze_qiji({
        "主孰有道": "我方领导更有感召力",
        "将孰有能": "对方管理者经验更丰富",
        "天地孰得": "我方地利优势明显",
        "法令孰行": "我方执行力更强",
        "兵众孰强": "对方资源更雄厚",
        "士卒孰练": "我方团队更专业",
        "赏罚孰明": "势均力敌"
    })
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 知彼知己分析示例
    print("\n" + "=" * 50)
    print("【知彼知己分析】")
    print("=" * 50)
    result = analyzer.analyze_situation(
        my_strengths=["技术领先", "团队专业", "品牌认知"],
        my_weaknesses=["资金不足", "渠道有限"],
        opp_strengths=["资金雄厚", "渠道广泛"],
        opp_weaknesses=["技术落后", "响应慢"],
        opportunities=["市场增长", "政策支持"],
        threats=["新进入者", "价格战"]
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()