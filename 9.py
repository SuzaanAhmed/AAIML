import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_block(ax, xy, text, color="#ADD8E6"):
    rect = patches.Rectangle(xy, 2, 1, linewidth=2, edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    ax.text(xy[0] + 0.9, xy[1] + 0.4, text, ha='center', va='center', fontsize=10)

def visualize_transformer():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Encoder Stack
    draw_block(ax, (1, 4.5), "Embedding")
    draw_block(ax, (1, 3.5), "Positional\nEncoding")

    draw_block(ax, (1, 2.5), "Self\nAttention", color="#90EE90")
    draw_block(ax, (1, 1.5), "Feed\nForward")

    ax.text(1.9, 0.6, "ENCODER", fontsize=12, weight='bold')

    # Decoder Stack
    draw_block(ax, (8, 4.5), "Embedding")
    draw_block(ax, (8, 3.5), "Positional\nEncoding")

    draw_block(ax, (8, 2.5), "Masked Self\nAttention", color="#FFB6C1")
    draw_block(ax, (8, 1.5), "Encoder-Decoder\nAttention", color="#FFA07A")
    draw_block(ax, (8, 0.5), "Feed\nForward")

    ax.text(8.9, 0.1, "DECODER", fontsize=12, weight='bold')

    # Attention Arrows
    ax.annotate("", xy=(2.9,2.9), xytext=(8,1.7),
                arrowprops=dict(arrowstyle="<->", lw=2))

    ax.text(5.5, 2.3, "Attention", fontsize=10)

    plt.title("Transformer Architecture Visualization", fontsize=16)
    plt.show()

# Run the visualization
visualize_transformer()


'''
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def block(ax, x, y, text, color):
    rect = patches.Rectangle((x, y), 2, 1, edgecolor="black",
                             facecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + 1, y + 0.5, text, ha='center', va='center', fontsize=10)

def transformer_diagram():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')

    # Encoder
    block(ax, 1, 4, "Embedding", "#ADD8E6")
    block(ax, 1, 3, "Positional\nEncoding", "#ADD8E6")
    block(ax, 1, 2, "Self\nAttention", "#90EE90")
    block(ax, 1, 1, "Feed\nForward", "#ADD8E6")

    ax.text(2, 0.5, "ENCODER", fontsize=12, weight='bold')

    # Decoder
    block(ax, 9, 4, "Embedding", "#FFCCCB")
    block(ax, 9, 3, "Positional\nEncoding", "#FFCCCB")
    block(ax, 9, 2, "Masked Self\nAttention", "#FF9999")
    block(ax, 9, 1, "Encoder-Decoder\nAttention", "#FFA07A")
    block(ax, 9, 0, "Feed\nForward", "#FFCCCB")

    ax.text(10, -0.5, "DECODER", fontsize=12, weight='bold')

    # Arrow between encoder attention & decoder attention
    ax.annotate("", xy=(3,2.5), xytext=(9,1.5),
                arrowprops=dict(arrowstyle="<->", lw=2))

    ax.text(5.8, 2.2, "Attention Flow", fontsize=10)

    plt.title("Transformer Architecture Visualization", fontsize=16)
    plt.show()

# Run
transformer_diagram()
'''