def hide_all_layers(image=gimp.image_list()[0]):
    for layer in image.layers:
        layer.visible = False


def show_all_layers(image=gimp.image_list()[0]):
    for layer in image.layers:
        layer.visible = True


def merge_every_nth_layers(n, image=gimp.image_list()[0]):
    hide_all_layers(image)
    group_size = len(image.layers) / n
    delta = n
    offset = 1
    for i in range(0, n):
        for j in range(0, group_size):
            image.layers[len(image.layers) - delta *
                         j - offset].visible = True
        pdb.gimp_image_merge_visible_layers(image, 0)
        image.layers[len(image.layers) - offset].visible = False
        delta -= 1
        offset += 1
    show_all_layers(image)


def merge_layers(layers, image=gimp.image_list()[0]):
    # layers - Array containing the layer's indexes.
    hide_all_layers(image)
    for layer in layers:
        image.layers[layer].visible = True
    pdb.gimp_image_merge_visible_layers(image, 0)
    show_all_layers(image)
