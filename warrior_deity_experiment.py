#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Warrior Deity Correspondence Experiment
A PsychoPy experiment demonstrating the Identity Functor framework
二郎神 (Erlang Shen) ↔ Archangel Michael

This experiment presents the correspondence between warrior deities across
Chinese and Abrahamic traditions as a visual demonstration of the identity
functor in categorical theology.
"""

from psychopy import visual, core, event
import sys

def create_experiment():
    """Create and run the Warrior Deity Correspondence experiment."""
    
    # Create a window
    win = visual.Window(
        size=[1200, 800],
        fullscr=False,
        screen=0,
        allowGUI=True,
        color=[0, 0, 0],
        units='height'
    )
    
    # Title
    title = visual.TextStim(
        win,
        text="Warrior Deity Correspondence\n二郎神 ↔ Archangel Michael\nIdentity Functor",
        pos=[0, 0.45],
        height=0.04,
        color='white',
        bold=True
    )
    
    # Instructions
    instruction = visual.TextStim(
        win,
        text="Press SPACE for detailed view | LEFT/RIGHT to focus | ESC to exit",
        pos=[0, -0.45],
        height=0.025,
        color='gray'
    )
    
    # Left side - Erlang Shen (二郎神)
    erlang_title = visual.TextStim(
        win,
        text="二郎神 (Erlang Shen)",
        pos=[-0.3, 0.3],
        height=0.045,
        color='gold',
        bold=True
    )
    
    erlang_tradition = visual.TextStim(
        win,
        text="Chinese (Taoist/Folk)",
        pos=[-0.3, 0.24],
        height=0.03,
        color='orange'
    )
    
    erlang_props = [
        "Three-eyed warrior god",
        "Defeats demons",
        "Controls floods",
        "Celestial hound companion",
        "Maintains cosmic order"
    ]
    
    erlang_properties = []
    y_pos = 0.15
    for prop in erlang_props:
        text_stim = visual.TextStim(
            win,
            text=f"• {prop}",
            pos=[-0.3, y_pos],
            height=0.028,
            color='lightblue',
            alignText='left'
        )
        erlang_properties.append(text_stim)
        y_pos -= 0.06
    
    # Right side - Archangel Michael
    michael_title = visual.TextStim(
        win,
        text="Archangel Michael",
        pos=[0.3, 0.3],
        height=0.045,
        color='gold',
        bold=True
    )
    
    michael_tradition = visual.TextStim(
        win,
        text="Abrahamic (Judaism/Christianity/Islam)",
        pos=[0.3, 0.24],
        height=0.03,
        color='orange'
    )
    
    michael_props = [
        "Chief of heavenly armies",
        "Defeats Satan and demons",
        "Warrior angel protector",
        "Defender of divine order",
        "Guardian of the faithful"
    ]
    
    michael_properties = []
    y_pos = 0.15
    for prop in michael_props:
        text_stim = visual.TextStim(
            win,
            text=f"• {prop}",
            pos=[0.3, y_pos],
            height=0.028,
            color='lightblue',
            alignText='left'
        )
        michael_properties.append(text_stim)
        y_pos -= 0.06
    
    # Center arrow showing correspondence
    arrow = visual.TextStim(
        win,
        text="↔",
        pos=[0, 0.05],
        height=0.08,
        color='cyan',
        bold=True
    )
    
    # Identity functor label
    identity_label = visual.TextStim(
        win,
        text="Identity Functor\n(Structure Preservation)",
        pos=[0, -0.05],
        height=0.03,
        color='lightgreen'
    )
    
    # Detailed explanation (shown on space)
    detailed_explanation = visual.TextStim(
        win,
        text="""Categorical Correspondence:
        
1. Warrior Archetype: Both are divine warriors
2. Protective Function: Both defend against evil
3. Active Intervention: Both engage in cosmic battles
4. Maintaining Order: Both uphold divine/cosmic law

The identity functor preserves essential properties
across different cultural contexts.""",
        pos=[0, -0.25],
        height=0.025,
        color='white',
        wrapWidth=1.5
    )
    
    # State variables
    showing_details = False
    focus_mode = None  # None, 'left', or 'right'
    clock = core.Clock()
    
    while True:
        # Check for key presses
        keys = event.getKeys(['space', 'escape', 'left', 'right'])
        
        if 'escape' in keys:
            break
        elif 'space' in keys:
            showing_details = not showing_details
        elif 'left' in keys:
            focus_mode = 'left' if focus_mode != 'left' else None
        elif 'right' in keys:
            focus_mode = 'right' if focus_mode != 'right' else None
        
        # Draw title and instruction
        title.draw()
        instruction.draw()
        
        # Determine opacity based on focus mode
        left_opacity = 1.0
        right_opacity = 1.0
        if focus_mode == 'left':
            right_opacity = 0.3
        elif focus_mode == 'right':
            left_opacity = 0.3
        
        # Draw Erlang Shen (left side)
        erlang_title.opacity = left_opacity
        erlang_title.draw()
        erlang_tradition.opacity = left_opacity
        erlang_tradition.draw()
        for prop in erlang_properties:
            prop.opacity = left_opacity
            prop.draw()
        
        # Draw Archangel Michael (right side)
        michael_title.opacity = right_opacity
        michael_title.draw()
        michael_tradition.opacity = right_opacity
        michael_tradition.draw()
        for prop in michael_properties:
            prop.opacity = right_opacity
            prop.draw()
        
        # Draw center elements
        arrow.draw()
        identity_label.draw()
        
        # Draw detailed explanation if toggled
        if showing_details:
            detailed_explanation.draw()
        
        # Update the window
        win.flip()
        
        # Check if window was closed
        if not win._closed:
            continue
        else:
            break
    
    # Cleanup
    win.close()
    core.quit()

if __name__ == "__main__":
    try:
        create_experiment()
    except Exception as e:
        print(f"Error running experiment: {e}")
        sys.exit(1)
