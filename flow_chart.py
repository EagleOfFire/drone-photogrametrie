import graphviz

def generate_flowchart():
    dot = graphviz.Digraph()

    dot.node('A', 'Start')
    dot.node('B', 'angle = 0')
    dot.node('C', 'Turn off/on video stream')
    dot.node('D', 'angle < 360?')
    dot.node('E', 'Rotate clockwise (angle)')
    dot.node('F', 'Move left (3)')
    dot.node('G', 'Capture & Save Image')
    dot.node('H', 'Increment angle by 1')
    dot.node('I', 'Wait for 1s')
    dot.node('J', 'Check key press')
    dot.node('K', 'Break if ESC/n')
    dot.node('L', 'Turn off video stream')
    dot.node('M', 'End')

    dot.edges(['AB', 'BC', 'CD'])
    dot.edge('D', 'E', label='Yes')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K', label='ESC/n Pressed')
    dot.edge('K', 'L')
    dot.edge('J', 'D', label='No')
    dot.edge('D', 'L', label='No')
    dot.edge('L', 'M')

    return dot

dot = generate_flowchart()
dot.render('orbit_flowchart', format='png', cleanup=True)
