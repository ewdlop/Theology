#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topological Defect Visualization Experiment
A PsychoPy experiment demonstrating topological defects in theological framework

This experiment visualizes the four types of topological defects and their
theological interpretations.
"""

from psychopy import visual, core, event
import sys
import math


def create_topological_defect_experiment():
    """Create and run the Topological Defect visualization experiment."""
    
    # Create a window
    win = visual.Window(
        size=[1400, 900],
        fullscr=False,
        screen=0,
        allowGUI=True,
        color=[0.05, 0.05, 0.1],
        units='height'
    )
    
    # Create text stimuli
    title = visual.TextStim(
        win,
        text="Topological Defects in Theological Framework\nSymmetry Breaking and Divine Structures",
        pos=[0, 0.45],
        height=0.035,
        color='white',
        bold=True
    )
    
    instruction = visual.TextStim(
        win,
        text="Press 1-4 for defect types | SPACE for overview | ESC to exit",
        pos=[0, -0.47],
        height=0.022,
        color='lightgray'
    )
    
    # Overview text
    overview_text = visual.TextStim(
        win,
        text=(
            "TOPOLOGICAL DEFECTS: Stable structures from symmetry breaking\n\n"
            "1 - MONOPOLE (0D): The Incarnation\n"
            "     Point singularity where infinite meets finite\n\n"
            "2 - VORTEX (1D): Prophetic Lineage\n"
            "     Linear axis through time with spiritual circulation\n\n"
            "3 - DOMAIN WALL (2D): Denominational Boundaries\n"
            "     Surface separating theological phases\n\n"
            "4 - TEXTURE (3D): Doctrinal Interpretation\n"
            "     Volume-filling hermeneutical landscape"
        ),
        pos=[0, 0],
        height=0.028,
        color='lightcyan',
        wrapWidth=1.3,
        alignText='left'
    )
    
    # Defect type displays
    # 1. Monopole
    monopole_title = visual.TextStim(
        win,
        text="MONOPOLE (0D Point Defect)",
        pos=[0, 0.35],
        height=0.04,
        color='red',
        bold=True
    )
    
    monopole_concept = visual.TextStim(
        win,
        text="The Incarnation",
        pos=[0, 0.28],
        height=0.045,
        color='orange'
    )
    
    monopole_desc = visual.TextStim(
        win,
        text=(
            "Symmetry Broken: Divine Unity\n"
            "Homotopy: π₂(S²) = ℤ\n\n"
            "• Point-like manifestation of infinity\n"
            "• Breaks transcendence-immanence symmetry\n"
            "• Topologically stable singularity\n"
            "• Divine concentrated at spacetime point\n"
            "• Cannot be removed continuously"
        ),
        pos=[0, 0.05],
        height=0.026,
        color='lightyellow',
        wrapWidth=1.2,
        alignText='left'
    )
    
    # Visual representation: central point with radiating field
    monopole_center = visual.Circle(
        win,
        radius=0.03,
        pos=[0, -0.15],
        fillColor='red',
        lineColor='orange',
        lineWidth=2
    )
    
    # Radiating circles
    monopole_circles = []
    for i in range(1, 5):
        circle = visual.Circle(
            win,
            radius=0.03 + i * 0.04,
            pos=[0, -0.15],
            fillColor=None,
            lineColor='orange',
            lineWidth=1,
            opacity=1.0 - i * 0.2
        )
        monopole_circles.append(circle)
    
    # 2. Vortex
    vortex_title = visual.TextStim(
        win,
        text="VORTEX/STRING (1D Line Defect)",
        pos=[0, 0.35],
        height=0.04,
        color='cyan',
        bold=True
    )
    
    vortex_concept = visual.TextStim(
        win,
        text="Prophetic Lineage",
        pos=[0, 0.28],
        height=0.045,
        color='lightblue'
    )
    
    vortex_desc = visual.TextStim(
        win,
        text=(
            "Symmetry Broken: Temporal Continuity\n"
            "Homotopy: π₁(S¹) = ℤ\n\n"
            "• One-dimensional line through time\n"
            "• Spiritual circulation around axis\n"
            "• Protected by winding number\n"
            "• Connects past and future\n"
            "• Cannot be unwound continuously"
        ),
        pos=[0, 0.05],
        height=0.026,
        color='lightcyan',
        wrapWidth=1.2,
        alignText='left'
    )
    
    # Visual representation: vertical line with circulation
    vortex_line = visual.Line(
        win,
        start=[0, -0.3],
        end=[0, 0],
        lineColor='cyan',
        lineWidth=3
    )
    
    # Circular arrows around line
    vortex_arrows = []
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x = 0.08 * math.cos(rad)
        y = -0.15 + 0.08 * math.sin(rad)
        arrow = visual.TextStim(
            win,
            text="→",
            pos=[x, y],
            height=0.04,
            color='lightblue',
            ori=-angle
        )
        vortex_arrows.append(arrow)
    
    # 3. Domain Wall
    wall_title = visual.TextStim(
        win,
        text="DOMAIN WALL (2D Surface Defect)",
        pos=[0, 0.35],
        height=0.04,
        color='green',
        bold=True
    )
    
    wall_concept = visual.TextStim(
        win,
        text="Denominational Boundaries",
        pos=[0, 0.28],
        height=0.045,
        color='lightgreen'
    )
    
    wall_desc = visual.TextStim(
        win,
        text=(
            "Symmetry Broken: Universal Church\n"
            "Homotopy: π₀ (discrete)\n\n"
            "• Surface separating traditions\n"
            "• Marks theological phase transition\n"
            "• Energy barrier to cross\n"
            "• Can merge (ecumenism) or persist (schism)\n"
            "• Represents historical divisions"
        ),
        pos=[0, 0.05],
        height=0.026,
        color='palegreen',
        wrapWidth=1.2,
        alignText='left'
    )
    
    # Visual representation: vertical wall separating regions
    wall_surface = visual.Rect(
        win,
        width=0.01,
        height=0.35,
        pos=[0, -0.15],
        fillColor='green',
        lineColor='lightgreen',
        lineWidth=2
    )
    
    wall_left_label = visual.TextStim(
        win,
        text="Phase A",
        pos=[-0.15, -0.15],
        height=0.03,
        color='lightgreen'
    )
    
    wall_right_label = visual.TextStim(
        win,
        text="Phase B",
        pos=[0.15, -0.15],
        height=0.03,
        color='lightgreen'
    )
    
    # 4. Texture
    texture_title = visual.TextStim(
        win,
        text="TEXTURE (3D Volume Defect)",
        pos=[0, 0.35],
        height=0.04,
        color='magenta',
        bold=True
    )
    
    texture_concept = visual.TextStim(
        win,
        text="Doctrinal Interpretation Space",
        pos=[0, 0.28],
        height=0.045,
        color='violet'
    )
    
    texture_desc = visual.TextStim(
        win,
        text=(
            "Symmetry Broken: Unified Interpretation\n"
            "Homotopy: π₃(S³) = ℤ\n\n"
            "• Volume-filling configuration\n"
            "• Gradual variation across space\n"
            "• No sharp boundaries\n"
            "• Hermeneutical complexity\n"
            "• Maps interpretation landscape"
        ),
        pos=[0, 0.05],
        height=0.026,
        color='plum',
        wrapWidth=1.2,
        alignText='left'
    )
    
    # Visual representation: gradient field
    texture_points = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            x = i * 0.06
            y = -0.15 + j * 0.05
            intensity = 0.3 + 0.7 * (1 - math.sqrt((i/3)**2 + (j/3)**2) / math.sqrt(2))
            point = visual.Circle(
                win,
                radius=0.015,
                pos=[x, y],
                fillColor=[intensity, 0, intensity],
                lineColor=None
            )
            texture_points.append(point)
    
    # Animation variables
    current_view = 'overview'  # 'overview', 'monopole', 'vortex', 'wall', 'texture'
    animation_time = 0
    
    clock = core.Clock()
    
    # Main experiment loop
    while True:
        # Check for key presses
        keys = event.getKeys(['escape', 'space', '1', '2', '3', '4'])
        
        if 'escape' in keys:
            break
        elif 'space' in keys:
            current_view = 'overview'
        elif '1' in keys:
            current_view = 'monopole'
        elif '2' in keys:
            current_view = 'vortex'
        elif '3' in keys:
            current_view = 'wall'
        elif '4' in keys:
            current_view = 'texture'
        
        # Update animation
        animation_time = clock.getTime()
        pulse = (math.sin(animation_time * 2) + 1) / 2  # 0 to 1 oscillation
        
        # Draw title and instruction
        title.draw()
        instruction.draw()
        
        if current_view == 'overview':
            overview_text.draw()
        
        elif current_view == 'monopole':
            monopole_title.draw()
            monopole_concept.draw()
            monopole_desc.draw()
            
            # Animate monopole
            monopole_center.draw()
            for i, circle in enumerate(monopole_circles):
                circle.opacity = (1.0 - i * 0.2) * (0.5 + 0.5 * pulse)
                circle.draw()
        
        elif current_view == 'vortex':
            vortex_title.draw()
            vortex_concept.draw()
            vortex_desc.draw()
            
            # Animate vortex
            vortex_line.draw()
            for i, arrow in enumerate(vortex_arrows):
                arrow.opacity = 0.3 + 0.7 * math.sin(animation_time * 2 + i * math.pi / 4)
                arrow.draw()
        
        elif current_view == 'wall':
            wall_title.draw()
            wall_concept.draw()
            wall_desc.draw()
            
            # Animate wall
            wall_surface.opacity = 0.5 + 0.5 * pulse
            wall_surface.draw()
            wall_left_label.draw()
            wall_right_label.draw()
        
        elif current_view == 'texture':
            texture_title.draw()
            texture_concept.draw()
            texture_desc.draw()
            
            # Animate texture
            for point in texture_points:
                point.draw()
        
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
        create_topological_defect_experiment()
    except Exception as e:
        print(f"Error running experiment: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
