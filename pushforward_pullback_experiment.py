#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pushforward-Pullback Visualization Experiment
A PsychoPy experiment demonstrating categorical theology concepts

This experiment visualizes the relationship between:
- Pushforward (Maitreya): Future-oriented, covariant transformation
- Pullback (Messiah): Past-referencing, contravariant transformation
"""

from psychopy import visual, core, event
import sys
import math


def create_pushforward_pullback_experiment():
    """Create and run the Pushforward-Pullback visualization experiment."""
    
    # Create a window
    win = visual.Window(
        size=[1200, 800],
        fullscr=False,
        screen=0,
        allowGUI=True,
        color=[0.1, 0.1, 0.15],
        units='height'
    )
    
    # Create text stimuli
    title = visual.TextStim(
        win,
        text="Categorical Theology\nPushforward ↔ Pullback :: Maitreya ↔ Messiah",
        pos=[0, 0.42],
        height=0.04,
        color='white',
        bold=True
    )
    
    instruction = visual.TextStim(
        win,
        text="Press SPACE to toggle views | LEFT/RIGHT arrows to switch focus | ESC to exit",
        pos=[0, -0.45],
        height=0.025,
        color='lightgray'
    )
    
    # Pushforward (Maitreya) - Left side
    pushforward_title = visual.TextStim(
        win,
        text="PUSHFORWARD (Covariant)",
        pos=[-0.4, 0.32],
        height=0.035,
        color='cyan',
        bold=True
    )
    
    maitreya_label = visual.TextStim(
        win,
        text="Maitreya",
        pos=[-0.4, 0.25],
        height=0.045,
        color='lightblue'
    )
    
    pushforward_desc = visual.TextStim(
        win,
        text="Future Buddha\nPresent → Future\nForward projection",
        pos=[-0.4, 0.12],
        height=0.028,
        color='lightcyan',
        wrapWidth=0.35
    )
    
    # Arrow pointing forward (right)
    pushforward_arrow = visual.TextStim(
        win,
        text="→ → →",
        pos=[-0.4, -0.05],
        height=0.06,
        color='cyan'
    )
    
    pushforward_properties = visual.TextStim(
        win,
        text="• Covariant functor\n• Preserves direction\n• Hope for future\n• Dharma teaching ahead",
        pos=[-0.4, -0.2],
        height=0.025,
        color='paleturquoise',
        wrapWidth=0.35,
        alignText='left'
    )
    
    # Pullback (Messiah) - Right side
    pullback_title = visual.TextStim(
        win,
        text="PULLBACK (Contravariant)",
        pos=[0.4, 0.32],
        height=0.035,
        color='orange',
        bold=True
    )
    
    messiah_label = visual.TextStim(
        win,
        text="Messiah",
        pos=[0.4, 0.25],
        height=0.045,
        color='gold'
    )
    
    pullback_desc = visual.TextStim(
        win,
        text="Prophetic Fulfillment\nFuture ← Past\nBackward reference",
        pos=[0.4, 0.12],
        height=0.028,
        color='lightyellow',
        wrapWidth=0.35
    )
    
    # Arrow pointing backward (left)
    pullback_arrow = visual.TextStim(
        win,
        text="← ← ←",
        pos=[0.4, -0.05],
        height=0.06,
        color='orange'
    )
    
    pullback_properties = visual.TextStim(
        win,
        text="• Contravariant functor\n• Reverses direction\n• Ancient covenant\n• Prophecy fulfilled",
        pos=[0.4, -0.2],
        height=0.025,
        color='peachpuff',
        wrapWidth=0.35,
        alignText='left'
    )
    
    # Central duality explanation
    duality_text = visual.TextStim(
        win,
        text="↔ CATEGORICAL DUALITY ↔",
        pos=[0, 0],
        height=0.03,
        color='white',
        bold=True
    )
    
    # Detailed view (shown on space press)
    detailed_view = visual.TextStim(
        win,
        text=(
            "TEMPORAL MEDIATION\n\n"
            "Maitreya (Pushforward):\n"
            "Current practice → Future enlightenment\n"
            "Covariant with time's arrow\n\n"
            "Messiah (Pullback):\n"
            "Current redemption ← Ancient promise\n"
            "Contravariant validation\n\n"
            "Together: Complete eschatological framework"
        ),
        pos=[0, 0],
        height=0.028,
        color='lightgreen',
        wrapWidth=0.8
    )
    
    # Focus indicators (circles)
    focus_left = visual.Circle(
        win,
        radius=0.42,
        pos=[-0.4, 0.05],
        lineColor='cyan',
        lineWidth=3,
        fillColor=None
    )
    
    focus_right = visual.Circle(
        win,
        radius=0.42,
        pos=[0.4, 0.05],
        lineColor='orange',
        lineWidth=3,
        fillColor=None
    )
    
    # Animation variables
    showing_detailed = False
    focus_side = 'both'  # 'left', 'right', or 'both'
    animation_time = 0
    
    clock = core.Clock()
    
    # Main experiment loop
    while True:
        # Check for key presses
        keys = event.getKeys(['space', 'escape', 'left', 'right'])
        
        if 'escape' in keys:
            break
        elif 'space' in keys:
            showing_detailed = not showing_detailed
        elif 'left' in keys:
            focus_side = 'left' if focus_side != 'left' else 'both'
        elif 'right' in keys:
            focus_side = 'right' if focus_side != 'right' else 'both'
        
        # Update animation
        animation_time = clock.getTime()
        pulse = (math.sin(animation_time * 2) + 1) / 2  # 0 to 1 oscillation
        
        # Draw title and instruction
        title.draw()
        instruction.draw()
        
        if showing_detailed:
            # Show detailed view
            detailed_view.draw()
        else:
            # Show main view
            if focus_side in ['left', 'both']:
                pushforward_title.draw()
                maitreya_label.draw()
                pushforward_desc.draw()
                
                # Animate arrow
                pushforward_arrow.opacity = 0.5 + 0.5 * pulse
                pushforward_arrow.draw()
                
                pushforward_properties.draw()
                
                if focus_side == 'left':
                    focus_left.draw()
            
            if focus_side in ['right', 'both']:
                pullback_title.draw()
                messiah_label.draw()
                pullback_desc.draw()
                
                # Animate arrow
                pullback_arrow.opacity = 0.5 + 0.5 * (1 - pulse)
                pullback_arrow.draw()
                
                pullback_properties.draw()
                
                if focus_side == 'right':
                    focus_right.draw()
            
            if focus_side == 'both':
                duality_text.draw()
        
        # Update the window
        win.flip()
        
        # Check if window was closed
        if win._closed:
            break
    
    # Cleanup
    win.close()
    core.quit()


if __name__ == "__main__":
    try:
        create_pushforward_pullback_experiment()
    except Exception as e:
        print(f"Error running experiment: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
