from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

# generate some random predictions and true labels

def draw(y_true, y_pred, name, classes):
    # define the class labels
    # compute the confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    # create the figure and axes with a larger size
    fig, ax = plt.subplots(figsize=(6, 4))

    # create the heatmap
    im = ax.imshow(cm, cmap='Blues', interpolation='nearest')

    # add the colorbar
    cbar = ax.figure.colorbar(im, ax=ax)

    # set the axis labels and tick labels
    ax.set_xticks(np.arange(len(classes)))
    ax.set_yticks(np.arange(len(classes)))
    ax.set_xticklabels(classes, rotation=50)
    ax.set_yticklabels(classes)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')

    # add the annotations
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    # add the title
    ax.set_title('Confusion Matrix')

    # adjust the layout
    fig.tight_layout()
    # save the figure as a PNG file with 300 dpi resolution
    fig.savefig('confusion_matrix_' + name + '.png', dpi=300)

    # show the plot
    plt.show()