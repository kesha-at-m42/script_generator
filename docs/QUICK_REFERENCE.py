"""
Quick visual reference for module editor
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                    📝 MODULE EDITOR QUICK GUIDE                      ║
╚══════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────┐
│  🚀 LAUNCH                                                           │
├──────────────────────────────────────────────────────────────────────┤
│  streamlit run dashboard/run_module_editor.py                        │
│  OR: Double-click run_module_editor.bat (Windows)                    │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  📍 WHERE IS THE SAVE BUTTON?                                        │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  1. Select your module from dropdown at top                          │
│  2. Edit fields in any tab (1-7)                                     │
│  3. Go to TAB 8: "Save & Export"  ⬅️ SAVE BUTTON IS HERE            │
│  4. Click the big blue "Save Changes" button                         │
│  5. ✅ Success! Changes written to inputs/modules.py                 │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  ➕ ADD NEW MODULE                                                    │
├──────────────────────────────────────────────────────────────────────┤
│  1. Click "➕ New Module" button (top right)                         │
│  2. New module appears in dropdown                                   │
│  3. Edit the fields                                                  │
│  4. ⚠️  IMPORTANT: Go to tab 8 and click "Save Changes"             │
│     (Otherwise it only exists in memory!)                            │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  🗑️  DELETE MODULE                                                    │
├──────────────────────────────────────────────────────────────────────┤
│  1. Select module from dropdown                                      │
│  2. Go to tab 8: "Save & Export"                                     │
│  3. Click "Delete Module" button                                     │
│  4. Click again to confirm                                           │
│  5. Click "Save Changes" to persist deletion                         │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  🔄 SWITCH BETWEEN MODULES                                            │
├──────────────────────────────────────────────────────────────────────┤
│  1. Use dropdown at top                                              │
│  2. Fields automatically update                                      │
│  3. Your edits are preserved in memory                               │
│  4. Save when ready                                                  │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  📋 8 TABS EXPLAINED                                                  │
├──────────────────────────────────────────────────────────────────────┤
│  Tab 1: Basic Info           → Name, number, grade, variant         │
│  Tab 2: Learning Goals       → Verbatim goals list                  │
│  Tab 3: Vocabulary           → Key terms (one per line)             │
│  Tab 4: Standards            → Building on/Addressing/Toward         │
│  Tab 5: Core Concepts        → Main conceptual themes               │
│  Tab 6: Detailed Goals       → Full breakdown with examples         │
│  Tab 7: Misconceptions       → Common errors + corrections          │
│  Tab 8: Save & Export        → 💾 SAVE BUTTON HERE! 💾             │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  ⚠️  IMPORTANT REMINDERS                                             │
├──────────────────────────────────────────────────────────────────────┤
│  • Changes are NOT auto-saved                                        │
│  • You MUST click "Save Changes" in tab 8                            │
│  • New modules won't appear in modules.py until you save             │
│  • Deletions don't persist until you save                            │
│  • Use "Export Module" for JSON backups before major edits           │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  ✅ VERIFY YOUR CHANGES                                               │
├──────────────────────────────────────────────────────────────────────┤
│  After saving, check:                                                │
│  • Open inputs/modules.py in editor                                  │
│  • Run: python tests/demo_multiple_modules.py                        │
│  • Look at "Preview" section in tab 8                                │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  🎯 QUICK WORKFLOW                                                    │
├──────────────────────────────────────────────────────────────────────┤
│  1. Launch: streamlit run dashboard/run_module_editor.py             │
│  2. Select: Choose module from dropdown                              │
│  3. Edit: Change any fields in tabs 1-7                              │
│  4. Save: Go to tab 8, click "Save Changes"                          │
│  5. Verify: Check inputs/modules.py or run demo script               │
└──────────────────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════╗
║  💡 Remember: TAB 8 = SAVE TAB!                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")
