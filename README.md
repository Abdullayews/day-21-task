#Statistics Sinifi
#Bu sinif xarici modul olmadan, yalnız Python-un əsas imkanları ilə statistik hesablamalar aparır. Konstruktor (__init__) ədədlər siyahısını qəbul edib self.data-ya mənimsədir. Bütün metodlar həmin siyahı üzərində işləyir.
count, sum, min, max metodları sadə döngü ilə siyahını skan edir. mean orta qiyməti, median isə sıralanmış siyahının ortancıl elementini qaytarır — siyahının uzunluğu cüt olduqda iki ortancıl elementin ortası götürülür. mode hər dəyərin neçə dəfə təkrarlandığını lüğətdə saxlayır və ən yüksək tezlikli dəyəri tapır. var dispersiyanı hər elementin orta qiymətdən kvadratik fərqinin ortası kimi hesablayır; std isə onun kök qiymətidir. freq_dist hər dəyərin faiz payını hesablayıb azalan sıra ilə sıralayır. describe bütün metodları ardıcıl çağırıb nəticəni ekrana çap edir.

#PersonAccount Sinifi
#Bu sinif şəxsin maliyyə hesabını modelləşdirir. Konstruktorda ad-soyad qəbul edilir, incomes və expenses adlı iki boş siyahı yaradılır. Hər gəlir və xərc {'amount': ..., 'description': ...} formatında lüğət kimi həmin siyahılara əlavə edilir.
total_income və total_expense metodları müvafiq siyahılardakı bütün məbləğləri toplayır. account_balance bu iki cəm arasındakı fərqi qaytarır. account_info isə bütün məlumatları formatlaşdırılmış şəkildə ekrana çap edir.
