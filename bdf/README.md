<!-- -*- encoding: utf-8 -*- -->

フォントサイズを拡大したBDFは、Ubuntu Linux 18.04 LTS + bdfresize 1.5 を使って生成した。

```bash
bdfresize -f 2 pet2015bdf_x1.0.bdf > pet2015bdf_x2.0.bdf
bdfresize -f 3 pet2015bdf_x1.0.bdf > pet2015bdf_x3.0.bdf
bdfresize -f 4 pet2015bdf_x1.0.bdf > pet2015bdf_x4.0.bdf
bdfresize -f 5 pet2015bdf_x1.0.bdf > pet2015bdf_x5.0.bdf
bdfresize -f 3/2 pet2015bdf_x1.0.bdf > pet2015bdf_x1.5.bdf
bdfresize -f 5/2 pet2015bdf_x1.0.bdf > pet2015bdf_x2.5.bdf
bdfresize -f 7/2 pet2015bdf_x1.0.bdf > pet2015bdf_x3.5.bdf
bdfresize -f 9/2 pet2015bdf_x1.0.bdf > pet2015bdf_x4.5.bdf
```

