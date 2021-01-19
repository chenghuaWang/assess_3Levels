```python
M=cv2.getRotationMatrix2D(center, angle, scale)
```

> center：图片的旋转中心

> angle：旋转角度（在这段代码里取反向）

> scale：旋转后图像相比原来的缩放比例

> M:计算得到的旋转矩阵

**这个函数的作用是获得仿射变换矩阵**

```python
cv2.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]))
```

> img为待操作的图像

> rot_mat表示仿射变化矩阵

> (image.shape[1], image.shape[0])表示变换后的图片大小

**这个函数的目的是进行仿射变换**
