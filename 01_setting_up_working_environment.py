######################################
# python ilk adimlar
######################################

print('hello world')
print('Hello AI Era!')

# degiskenler ve tipleri
x = 3.14
type(x)
y = 'hakan'
type(y)
type(5)
type({'mustafa'})
type(('mustafa',))

# atamalar ve degiskenler
a = 'hakan'
type(a)

# degiskenler ile islem yapma
a = 9
b = 10
a * b
a - b
d = b - a

######################################
# sanal ortam ve paket yonetimi
######################################

"""
# sanal ortamlarin listelenmesi
    conda env list
    
# sanal ortam olusturma
    conda create -n ortam_adi

# olusturulan sanal ortami aktif etme
    conda activate ortam_adi

# olusturulan sanal ortami inaktif etme
    conda deactivate

# yüklü paketlerin listelenmesi
    conda list

# paket yükleme
    conda install paket_adi
    conda install numpy

# ayni anda birden fazla paket yükleme
    conda install paket_adi_1 paket_adi_2
    conda install scipy pandas

# paket silme ve silinen paketin ozel versiyonunu yükleme
    # silme islemi
    conda remove paket_adi
    conda remove numpy

    # belirli bir versiyona gore paket yükleme
    conda install paket_adi = versiyon
    conda install numpy = 1.20.1        # onceki versiyon yüklenir

# paket yükseltme-güncelleme
    conda upgrade paket_adi
    conda upgrade numpy

# tüm paketlerin güncellenmesi-yükseltilmesi
    conda upgrade -all

# pip ile paket yükleme
    pip install paket_adi
    pip install numpy

# pip ile belirli bir versiyona göre paket yükleme
    pip install paket_adi == versiyon

# kütüphaneleri bir arkadas veya baska bir calisma ortamina aktarma
    conda env export > environment.yaml

# inaktif yapilan ortamin silinmesi
    conda deactivate
    conda env remove -n ortam_adi

# var olan bir ortami yeniden ayaga kaldirmak
    conda env create -f environment.yaml

"""
