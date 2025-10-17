#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Divine Name Transformation Experiment
A PsychoPy experiment demonstrating the Id-Ego-Superego theological framework

This experiment presents the transformation from "yawhel elo elohim" to 
"yahweh leo leohim" as a visual demonstration of the psycho-theological concepts.
"""

from psychopy import visual, core, event
import sys

def create_experiment():
    """Create and run the Divine Name Transformation experiment."""
    
    # Create a window
    win = visual.Window(
        size=[1024, 768],
        fullscr=False,
        screen=0,
        allowGUI=True,
        color=[0, 0, 0],
        units='height'
    )
    
    # Create text stimuli
    title = visual.TextStim(
        win,
        text="Divine Name Transformation\nId-Ego-Superego Framework",
        pos=[0, 0.4],
        height=0.05,
        color='white',
        bold=True
    )
    
    instruction = visual.TextStim(
        win,
        text="Press SPACE to see transformation, ESC to exit",
        pos=[0, -0.4],
        height=0.03,
        color='gray'
    )
    
    # Original form
    original_text = visual.TextStim(
        win,
        text="yawhel elo elohim",
        pos=[0, 0.1],
        height=0.06,
        color='lightblue'
    )
    
    # Transformed form
    transformed_text = visual.TextStim(
        win,
        text="yahweh leo leohim",
        pos=[0, 0.1],
        height=0.06,
        color='lightgreen'
    )
    
    # Analysis labels
    superego_label = visual.TextStim(
        win,
        text="Superego: yahweh (Divine Authority)",
        pos=[0, -0.05],
        height=0.04,
        color='gold'
    )
    
    ego_label = visual.TextStim(
        win,
        text="Ego: leo (Mediating Function)",
        pos=[0, -0.15],
        height=0.04,
        color='orange'
    )
    
    id_label = visual.TextStim(
        win,
        text="Id: leohim (Primal Forces)",
        pos=[0, -0.25],
        height=0.04,
        color='red'
    )
    
    # Main experiment loop
    showing_original = True
    clock = core.Clock()
    
    while True:
        # Check for key presses
        keys = event.getKeys(['space', 'escape'])
        
        if 'escape' in keys:
            break
        elif 'space' in keys:
            showing_original = not showing_original
        
        # Draw title and instruction
        title.draw()
        instruction.draw()
        
        # Draw either original or transformed text
        if showing_original:
            original_text.draw()
        else:
            transformed_text.draw()
            # Show analysis only with transformed text
            superego_label.draw()
            ego_label.draw()
            id_label.draw()
        
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
