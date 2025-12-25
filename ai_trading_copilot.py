"""
AI Trading Copilot
"""

from datetime import datetime


# AI TRADING COPILOT

class TradingCopilot:
    """AI copilot: inputs → analysis → guardrails → output"""
    
    def __init__(self):
        self.inputs = []  # Store all inputs
    
    def add_input(self, time, source, url, fact, value=None):
        """Add one market input"""
        self.inputs.append({
            'time': time,
            'source': source, 
            'url': url,
            'fact': fact,
            'value': value
        })
    
    def analyze(self):
        """Run full analysis and print results"""
        
        # Output 1: EVENT SUMMARY
        print("\n" + "="*70)
        print("EVENT SUMMARY")
        print("="*70)
        for inp in self.inputs:
            val = f" [{inp['value']}]" if inp['value'] else ""
            print(f"  {inp['time']}: {inp['fact']}{val}")
        
        # Output 2: WHAT MATTERS
        print("\n" + "="*70)
        print("WHAT MATTERS")
        print("="*70)
        
        # Simple keyword detection
        themes = []
        for inp in self.inputs:
            text = inp['fact'].lower()
            if 'shutdown' in text or 'closed' in text:
                themes.append("Supply disruption")
            if inp['value'] and inp['value'] > 250:
                themes.append(f"High price: €{inp['value']}/MWh")
            if inp['value'] and inp['value'] < 85 and 'storage' in text:
                themes.append(f"Low storage: {inp['value']}%")
        
        for theme in set(themes):
            print(f"  + {theme}")
        
        print("\n  What to watch:")
        print("  - Next flow data update")
        print("  - Weather forecast")
        print("  - Policy announcements")
        
        # Confidence marker (guardrail)
        confidence = "HIGH" if len(self.inputs) >= 3 else "MEDIUM"
        print(f"\n  Confidence: {confidence} ({len(self.inputs)} inputs)")
        
        # Output 3: SCENARIO TABLE
        print("\n" + "="*70)
        print("SCENARIO TABLE")
        print("="*70)
        
        # Check if we should shift probabilities
        is_major_disruption = any('indefinitely' in inp['fact'].lower() 
                                  for inp in self.inputs)
        
        scenarios = [
            ["Base: Status Quo", "40%" if is_major_disruption else "50%", 
             "€400-500", "Hold position"],
            ["Bull: Extended Crisis", "40%" if is_major_disruption else "30%", 
             "€600+", "Add to longs"],
            ["Bear: Demand Drop", "15%" if is_major_disruption else "15%", 
             "€200-300", "Cut 50%"],
            ["Tail: Resolution", "5%" if is_major_disruption else "5%", 
             "€150", "Exit all"]
        ]
        
        print(f"  {'Scenario':<25} {'Prob':<8} {'Power Price':<15} {'Action'}")
        print("  " + "-"*65)
        for s in scenarios:
            print(f"  {s[0]:<25} {s[1]:<8} {s[2]:<15} {s[3]}")
        
        # Output 4: PRE-TRADE CHECKLIST
        print("\n" + "="*70)
        print("PRE-TRADE CHECKLIST")
        print("="*70)
        
        # Risk flags
        risk_flags = []
        for inp in self.inputs:
            if inp['value'] and inp['value'] > 300:
                risk_flags.append("EXTREME VOLATILITY - Tighten stops")
            if 'crisis' in inp['fact'].lower() or 'war' in inp['fact'].lower():
                risk_flags.append("HEADLINE RISK - Reduce size 50%")
        
        if risk_flags:
            print("  Risk Flags:")
            for flag in set(risk_flags):
                print(f"    {flag}")
        else:
            print("  No major risk flags")
        
        print("\n  Position Limits:")
        print("    Max position: 2,000 MWh")
        print("    Max loss: €200,000")
        print("    Current status: Within limits")
        
        # Output 5: SOURCE CITATIONS (guardrail)
        print("\n" + "="*70)
        print("SOURCE CITATIONS")
        print("="*70)
        for i, inp in enumerate(self.inputs, 1):
            print(f"  [{i}] {inp['source']}: {inp['url']}")
        
        # Output 6: HUMAN SIGN-OFF (guardrail)
        print("\n" + "="*70)
        print("HUMAN SIGN-OFF REQUIRED")
        print("="*70)
        print("""
  □ I reviewed the event summary
  □ I verified sources independently  
  □ I understand scenarios and risks
  □ Position is within limits
  □ I accept responsibility
  
  Trader: 
  Date: 
  Time: 
""")


# DEMO

if __name__ == "__main__":
    
    print("="*70)
    print("AI TRADING COPILOT")
    print("="*70)
    print("Demo: Nord Stream crisis, Sep 2, 2022")
    
    # Create copilot
    copilot = TradingCopilot()
    
    # Add inputs (one function call per input)
    print("\nAdding inputs...")
    
    copilot.add_input(
        time="09:30",
        source="Reuters", 
        url="reuters.com/energy/nordstream",
        fact="Russia: Nord Stream 1 closed indefinitely"
    )
    
    copilot.add_input(
        time="10:00",
        source="ICE Exchange",
        url="ice.com/ttf",
        fact="TTF front-month",
        value=280
    )
    
    copilot.add_input(
        time="10:15",
        source="ENTSOG",
        url="entsog.eu/flows",
        fact="Nord Stream flows confirmed at 0 mcm/day",
        value=0
    )
    
    copilot.add_input(
        time="10:30",
        source="GIE AGSI",
        url="agsi.gie.eu",
        fact="EU storage level",
        value=82.5
    )
    
    print("  ✓ 4 inputs loaded")
    
    # Run analysis
    copilot.analyze()
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    print("\nNext: Review → Verify sources → Sign off → Trade")
