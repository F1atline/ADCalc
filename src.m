script
prog='haradkz'; 
%          Базовый для расчета механических, электромеханических 
%                   и энергетических характеристик АДКЗ 
%                     при изменении U1, f1, I1, R1, X1 
                    
%                    Перед расчетами ПОВТОРИТЬ  главу
%    "Электромеханические свойства и характеристики асинхронного двигателя"

%                              РАССЧИТАТЬ:
%              - координаты заданных точек M1,w1 и M2,w2; 
%              - параметры  источника питания U1, f1 или I1,f1, или Ipost.
%             
%                               ВНИМАНИЕ!
%                 В этой программе  НИЧЕГО НЕ ИЗМЕНЯТЬ!!!!!!!!
%             При выполнении расчетов  данную отладочную программу 
%                        сохранить под другим именем

%                           РАБОТА С ПРОГРАММОЙ                        
%                      
%      1. Внимательно прочитайте свою программу, уясните алгоритм расчета.
%         Обозначения физических величин, примененные в программе, часто 
%         не совпадают с общепринятыми.Следует разобраться с их обозначениями.
%      2. Уравнения программы описаны в учебном пособии 
%         к курсовому проектированию по "Теории электропривода".
%      3. Ввести каталожные данные и обмоточные данные двигателя,
%         координаты заданной точки 
%      4. Выбрать источник питания и параметры выбранного источника 
%         Определитесь с необходимостью учета кривой намагничивания         
%      5. Ввести начальные условия:
%          - начальные wna и конечные wko скорости 
%          - шаг по скорости 
%      6. Начинать расчет следует с расчета естественных характеристик
%         Введите U1n, f1n, добавочные сопротивления Rd=0; Xd=0; R1d=0; X1d=0; 
%      7. Нажать клавишу Save and Run, далее OK      
%         О работе программы сигнализирует бегущая строка s=......
%         Результаты расчета выводятся в виде figure1. 
%         Убедитесь в правильности расчетов: Мк, при wн  М=Мн, I1=I1н, I2=I2н 
%      8. НЕ закрывайте  figure1. На нее будут выводиться результаты следующих
%         расчетов. Выберете нужные зависимости для вывода на печать
%      9. Введите предварительно рассчитанные изменения в программу:
%                - источник питания и его параметры
%                - коэффициент обратной связи по активной составляющей тока статора 
%                - добавочные сопротивления Rd=0; Xd=0; R1d=0; X1d=0;       
%                
%         Продолжайте расчет по п.п. 7
%         Сохраните figure1 для печати и дальнейшей обработки
%         результатов расчетов 

%         Каталожные данные двигателя

tip='4MTKF(H)200L6';  %Тип двигателя
pp=3;                  %Число пар полюсов
u1n=220;           %Номинальное фазное напряжение,В
f1n=50;               %Номинальная частота,Гц
Pn=22000;        %Номинальная мощность, Вт
nn=935;            %Номинальная скорость,об/мин
I1n=51;             %Номинальный ток статора,А 
kpdn=0.83;       %Номинальный кпд
cosfi1n=0.79;  %Номинальный cos fi1n
Mk=760;           %Критический момент, Нм
Mp=706;          %Пусковой момент,Нм
I1p=275;          %Пусковой ток статора, A

%Обмоточные данные двигателя 

%Если обмоточные данные отсутствуют, 
%можно рассчитать их приближенно в программе rxKZAD.m

r1=0.232;        %Cопротивление активное фазной обмотки СТАТОРА,Ом
r2p=0.325;      %Сопротивление активное приведенное фазной обмотки РОТОРА,Ом  
x1=0.285;         %Сопротивление индуктивное фазной обмотки СТАТОРА,Ом
x2p=0.2844;    %Сопротивление индуктивное приведенное фазной обмотки РОТОРА,Ом
Imn=26.3;        %Ток намагничивания номинальный, А  

%Выбрать источник питания

in=1             %Источник напряжения in=1
it=0              %Источник тока it=1
dt=0              %Динамическое торможение dt=1

%Задать параметры  источника питания

if in==1                %Источник напряжения in=1
   u1s=220;          %Фазное напряжение в заданной точке, В
   f1=50;                %Частота в заданной точке,Гц
end

if it==1                %Источник тока it=1
   i1s=55;           %Ток фазы статора в заданной точке, А
   f1=15;              %Частота в заданной точке,Гц
end

if dt==1                 %Динамическое торможение dt=1
   it==1; 
   f1=0;                  %Частота в заданной точке,Гц
   Ipost=100;       %Постоянный ток статора для заданной точки, А
   kc=0.816;         %Коэффициент схемы включения постоянного тока
   i1s=kc*Ipost;   %Эквивалентный переменный ток фазы статора 
end                      %для заданной точки, А  
    
    %Добавочные сопротивления статора, Ом
        R1d=0 
        X1d=0;
        
    kot=0;         %Коэффициент ПОС по активной составляющей тока статора:
                   % kot=1 - для компенсации скольжения s=sn 
      
    krn=1;         %При учете кривой намагничивания krn=1
     
         
%Расчетные данные двигателя
pi=3.1416;
won=2*pi*f1n/pp; %Номинальная синхронная скорость,рад/с
wn=nn/9.55;      %Номинальная скорость,рад/с
Mn=Pn/wn;        %Номинальный момент,Нм
sn=(won-wn)/won; %Номинальное скольжение
Mko=Mk/Mn;       %Критический момент, о.е.
Mpo=Mp/Mn;       %Пусковой момент, о.е.
I1po=I1p/I1n;    %Пусковой ток статора, о.е.
a1=r1/r2p;
sk=sn*(Mko+sqrt((Mko^2-1)+2*a1*sn*(Mko-1))/(1-2*sn*a1*(Mko-1)));
Memn=2*Mk*(1+a1*sk)/(sn/sk+sk/sn+2*a1*sk); %Номинальный электромагнитный момент,Нм
dMxn=Memn-Mn;         %Потери момента в номинальном режиме, Нм
r2v=Mp*won/(3*I1p^2); %Невыключаемое приведенное активное сопротивление ротора    
                      %c учетом вытеснения тока ротора ,Ом  
sinfi1n=sqrt(1-cosfi1n^2);
if Imn==0 
Imn=I1n*(sinfi1n-cosfi1n*sn/sk);%Ток намагничивания  в номинальном режиме, А
end                      
xmn=u1n/Imn-x1;%Индуктивное сопротивление контура намагничивания,Ом
E1n=Imn*xmn;   %Номинальная ЭДС статора, В
 r1=r1+R1d;;  x1=x1+X1d;
ks=0;
Im=Imn;
won=abs(won);% Для обратного вращения магнитного потока ввести -abs(won)

% Цикл расчета характеристики с шагом по скорости dw
       
    wna=-10;            %Начальная скорость, рад/с
    wko=110;            %Конечная скорость, рад/с   wn110
    dw=0.5;             %Шаг по скорости, рад/с

    M1=Mk;  w1=won*(1-sk);     %Координаты заданной точки 1
    M2=Mp; w2=0;     %Координаты заданной точки 2
    M3=I1p; w3=0;     %Координаты заданной точки 2

for w=wna:dw:wko;
    if dt==1, a=1;
       s=-w/won
       wo=won;
    else
       a=(f1+ks)/f1n;      %ks - Введение компенсации скольжения
       wo=a*won;
       s=(wo-w)/wo
    end

    if abs(s)<0.001, s=0.001;end 
    if krn==0
       xm=xmn;
    else
      imo=Im/Imn; 
    
    %Универсальная кривая намагничивания - 6 отрезков
    
      if imo<0.37 em=1.35*imo; end                  %kk=1.35;
      if imo>0.37 em=0.5+1.09*(imo-0.37); end       %kk=1.095; 
      if imo>0.6 em=0.75+0.625*(imo-0.6); end       %kk=0.625;
      if imo>1 em=1+0.5*(imo-1); end                %kk=0.5;
      if imo>1.2 em=1.1+0.167*(imo-1.2);end         %kk=0.167; 
      if imo>1.8 em=1.2+0.1*(imo-1.8); end          %kk=0.1;
      if em>1.3 em=1.3;end 
        
    xm=em*E1n/(imo*Imn);
end 
%   Расчет  Т-образной схемы замещения АД комплексным методом       

   r2s=(r2v)/s;
  % if (r2v-r2p)>0 r2s=(r2p+(r2v-r2p))/s; end %учет вытеснения тока ротора
   z2p=r2s+j*x2p*a;                          
   zm=j*xm*a;
   zmr=zm*z2p/(zm+z2p);
  
   z1=r1+j*x1*a;
   zc=z1+zmr;
   if dt==1,
      i2p=i1s*zm/(z2p+zm);
      I2p=abs(i2p);                             %Приведенный ток ротора,А     
      im=i1s*z2p/(z2p+zm);
      Im=abs(im);      
      I1=abs(i1s);                              %Ток статора, А
      I1a=real(i1s);
   else
      if it==1 i1=i1s; u1=i1*zc;end                               % Источник тока
      if in==1 u1=u1s+ks*u1n/f1n; i1=u1/zc;   end  % Источник напряжения
      I1=abs(i1);                                                            %Ток статора, А
      I1a=real(i1);
      e=i1*zmr;
      im=e/zm; 
      Im=abs(im);
      i2p=-e/z2p; 
      I2p=abs(i2p);                            %Приведенный ток ротора,А 
   end  

%Компенсация скольжения ks,Гц
   dfoi=f1n*I1a/(I1n*cosfi1n);       %Приращение частоты f1 от обратной связи  
if w>wo, dfoi=0; end                
   ks=kot*sn*dfoi;                            %по активной составляющей тока статора  
   
 %   Расчет момента, мощностей и энергетических показателей

   M=3*I2p^2*r2s/wo;             %Электромагнитный момент, нм
   if f1==0       cosfi=0;
   else
   cosfi=abs(cos(angle(zc))); %Коэффициент мощности двигателя
   end
   
   dMx=abs(dMxn)*sign(w);   %Реактивный момент х.х. двигателя                 
   Pv=(M-dMx)*w;                      %Мощность на валу, Вт
   dP2=3*I2p*I2p*r2p;             %Потери мощности в обмотках ротора, Вт
   Pem=M*w+dP2;                  %Мощность электромагнитная, Вт
   dP1=3*I1*I1*r1;                  %Потери мощности в обмотках статора, Вт
   Pc=3*abs(u1)*I1a;             %Мощность сети, Вт
  
   if dt==1
       Pc=0; kpd=0;
   else
   kpd=Pv/Pc;               % КПД
end
   if and(Pv<0,Pc<0), kpd=Pc/Pv;end    
   if or (M==0, w==0)   kpd=0;end
   if kpd <=0 kpd=0;end
   if kpd >1 kpd=0;end
     
   % Вывод характеристик на график (с 220 - 276)
  xlabel ('M,I1,Im,kpd,cosfi')
  ylabel ('w')  
    % Если какую-то из характеристик не нужно выводить на график,
    % поставьте знак % перед plot:   %plot()
       
  axis([-4 6 -1.5 1.8])       %рамка
  plot(M/Mn,w/abs(won),'k')
  plot(I1/I1n,w/abs(won),'b')
 % plot(I2p/I1n,w/abs(won),'r')
  %plot(Im/I1n,w/abs(won),'c')
 % plot(kpd,w/abs(won),'g')
  %plot(cosfi,w/abs(won),'m')
  plot(M1/Mn,w1/abs(won),'*r')
  plot(M2/Mn,w2/abs(won),'*r')
  plot(M3/I1n,w3/abs(won),'+r')
  hold on
  grid on
 
%*********************************
end
for i=-2.5:0.001:5.5 plot(i,0,'k'); end;  %оси
for i=-1.5:0.001:1.5 plot(0,i,'k'); end;
 
% Вывод на график номинальных данных двигателя

b14=num2str(Pn*10^(-3));
b15=num2str(Imn);
b19=num2str(won);
b20=num2str(Mn);
b21=num2str(I1n);
b22=num2str(kpdn);
b23=num2str(cosfi1n);

d=date;
text(3.8,-1.3,d,'color','k');
text(3.8,-1.2,prog,'color','k');
text(-3.8,1.6,tip,'color','k');
text(-1.7,1.6,'Pn =','color','k');
text(-1,1.6,b14,'color','k'); 
text(0.2,1.6,'won =','color','k');
text(1,1.6,b19,'color','k');
text(4.2,1.6,' I1n =','color','b');
text(5.1,1.6,b21,'color','b');
text(2.1,1.6,'Mn =','color','k');
text(2.8,1.6,b20,'color','k');
%text(4.2,1.4,' I2n =','color','r');
%text(5.1,1.4,b18,'color','r');
text(4.1,1.25,'kpdn=','color','g');
text(5.1,1.25,b22,'color','g');
text(4,1.1,'cosfin=','color','m');
text(5.1,1.1,b23,'color','m');

%end
%  y-Жё   m-Фи   c-Го   r-Кр   g-Зе   b-Си   w-Бе   k-Чё 

Pv
dMx
Pem
Im
I1
Pc
cosfi
kpd         
w
M
