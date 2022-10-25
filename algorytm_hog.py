import numpy as np
import cv2
Inport matplotlib.pyplot as plt

img = cv2.cvtcolor(cv2. inread("C:/users/4P/Docunents/police.ips"), cv2.COLOR_BGR2GRAY)

cell_size = (8, 8) # (h x w) w pikselach
block_size = (2, 2) #(h x w) w komomórkach
nbins = 9 # ilość ziaren orientacji

# winsize to rozmiar obrazu przyciętego do wielokrotności rozmiaru komórki
hog = cv2.HOGDescriptor(_winsize=(ing.shape[1] // cell_size[1] * cell_size[1],
                        img.shape[o] // cell_sizefe] * cell size[o]),
                        blocksize=(block_size[1] * cell_size[1],
                        block_size[0] * cell_size[0]},
                        _blockStride-(cell_size[1], cell_size[0]),
                        _CellSize=(cell_size[1], cell_size[0]),
                        _nbins=nbins)

 
ncells = (img.shape[0] // cell_size[o], ing-shape[1] // cell_size[1])
hog_feats = hog.conpute(img)\
                        .reshape(n_cells[1] - block size[1] + 1,
                                 n_cells[0] - block_size[0] + 1,
                                 block_size[0], block_size[1], nbins) \
                                 .transpose((1, @, 2, 3, 4)) # indeksować bloki według wierszy w pierwszej kolejności
# hog_feats zawiera teraz anplitudy gradientu dla każdego kierunku,
# dla każdej komórki swojej grupy dla każdej grupy. Indeksowanie odbywa się według wierszy, a następnie kolumn.

gradients = np.zeros((n_cells[0], n_celis[1], nbins))

# count cells (komórki graniczne pojawiają się rzadziej w nakładających się grupach)
cell_count = np.full((n_cells[e], n_celis[1], 1), @, dtype=int)

for off_y in range(block_size[0]):
    for off_x in range(block_size[1]):
        gradients[off_y:n_cells[0] - block_size[0] + off_y + 1,
                  off_x:n_cells[1] - block_size[1] + off_x + 1 += \
            hog_feats[:, :, off_y, off_x, :]        
        cell_count[off_y:n_cells[0] - block size[0] + off_y +1,
                   off_x:n_cells[1] - block size[1] + off_x + 1] += 1

# średni gradient
gradients /= cell_count
# podglad
plt.figure()
plt.inshow(img, cmap=" gray")
plt.show(),
bin = 5 
plt.peolor(gradients[:, :, bin])
plt.gca().invert_yaxis()
plt.gca().set_aspect('equal', adjustable="box")
plt.colorbar()
plt.show()
