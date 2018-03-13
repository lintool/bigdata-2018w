#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*
    seq seq10k run qrel err fneg fpos prev next x score
    1 0.000100 1 2 1 1 0 0 2 1.00000 0.520000
*/

#define SIZE 100

#define sq(x) ((x)*(x))

int FP,FN,H,S;
double lm,lam[SIZE], lama,lamsq;

double logit(double x){
   return log(x / (1-x));
}

int quant(double x) {
   if (x <= .0001) return 0;
   if (x <= .0002) return 1;
   if (x <= .0005) return 2;
   if (x <= .001) return 3;
   if (x <= .002) return 4;
   if (x <= .005) return 5;
   if (x <= .01) return 6;
   if (x <= .02) return 7;
   if (x <= .05) return 8;
   if (x <= .1) return 9;
   if (x <= .2) return 10;
   if (x <= .5) return 11;
   return 12;
}

double rquant[] = {.0001,.0002,.0005,.001,.002,.005,.01,.02,.05,.1,.2,.5,1};

double Xfpyfn[13], Xfnyfp[13];
double xfpyfn[SIZE][13], xfnyfp[SIZE][13];
double sfpyfn[13], sfnyfp[13];
double vfpyfn[13], vfnyfp[13];

struct ss {
   int run,qrel; double score;
} s[400000],t[400000];

comp(struct ss *a, struct ss *b){
   if (a->score > b->score) return 1;
   if (a->score < b->score) return -1;
   return 0;
   if (a->qrel == 2) return -1;
   return 1;
   return 0;
}

int i,j,k,m,n,hams,spams,cnt[51]; double inversions;
double roca,x[1000],maxx=-9999,minx=9999,meanx,varx,stdevx;
int thams, tspams;
double fp,fn;


double unlogit(double x) {
   double e = exp(x);
   return e/(1+e);
}

main(){
   scanf("%*[^\n]");
   thams = tspams = 0;
   for(n=0; 3 == scanf("%*s%d%lf%d",
                &t[n].qrel,&t[n].score,&t[n].run); n++) {
      t[n].score += random()*1e-20;
      if (t[n].qrel == 1) thams++; else tspams++;
   }
   hams = spams = fn = inversions = 0;
   for (i=0;i<13;i++) Xfpyfn[i] = Xfnyfp[i] = -1;
   qsort(t,n,sizeof(struct ss),comp);
   FP=FN=0;
   for (i=0;i<n;i++) {
      if (t[i].qrel == 1 && t[i].run != 1) FP++;
      if (t[i].qrel == 2 && t[i].run != 2) FN++;
      if (t[i].qrel == 1) hams++; else spams++;
      if (t[i].qrel == 1) inversions += spams;
      fp = thams - hams;
      if (fp == 0) fp = .5;
      fn = spams;
      if (fn == 0) fn = .5;
      Xfnyfp[quant((double)fn/tspams)] = (double)fp/thams;
      if (Xfpyfn[quant((double)fp/thams)] < 0) Xfpyfn[quant((double)fp/thams)] = (double)fn/tspams;
   }
   lm = (logit(FN/(double)(spams)) + logit(FP/(double)hams))/2;
   roca = (double)inversions/((double)hams*spams);
   if (roca == 0) roca = .5 / ((double)hams*spams);
   roca = log(roca/(1-roca));
   lama = lamsq = 0; 
   for (k=0;k<SIZE;k++) {
      thams = tspams = 0;
      for (i=0;i<13;i++) xfpyfn[k][i] = xfnyfp[k][i] = -1;
      for (i=0;i<n;i++) {
         s[i] = t[random()%n];
         s[i].score -= random()*1e-20;
         if (s[i].qrel == 1) thams++; else tspams++;
      }
      qsort(s,n,sizeof(struct ss),comp);
      hams = spams = fn = inversions = 0;
      FP=FN=0;
      for (i=0;i<n;i++) {
         if (s[i].qrel == 1 && s[i].run != 1) FP++;
         if (s[i].qrel == 2 && s[i].run != 2) FN++;
         if (s[i].qrel == 1) hams++; else spams++;
         if (s[i].qrel == 1) inversions += spams;
         fp = thams - hams;
         if (fp == 0) fp = .5;
         fn = spams;
         if (fn == 0) fn = .5;
         xfnyfp[k][quant((double)fn/tspams)] = (double)fp/thams;
         if (xfpyfn[k][quant((double)fp/thams)] < 0) xfpyfn[k][quant((double)fp/thams)] = (double)fn/tspams;
      }
      lam[k] = (logit(FN/(double)(spams)) + logit(FP/(double)hams))/2;
      lama += lam[k];
      x[k] = (double)inversions/((double)hams*spams);
      if (0 == x[k]) x[k] = .5/((double)hams*spams);
      x[k] = log(x[k]/(1-x[k]));
      if (x[k] > maxx) maxx = x[k];
      if (x[k] < minx) minx = x[k];
      meanx += x[k];
      for (i=0;i<13;i++) {
         sfpyfn[i] += logit(xfpyfn[k][i]);
         sfnyfp[i] += logit(xfnyfp[k][i]);
      }
   }
   lama /= SIZE;
   for (k=0;k<SIZE;k++) {
      lamsq += (lam[k]-lama)*(lam[k]-lama);
   }
   lamsq = sqrt(lamsq/(SIZE-1));
   //printf("lam%% %8.2lf (%0.2lf - %0.2lf)\n",100*unlogit(lm),100*unlogit(lm-1.96*lamsq),100*unlogit(lm+1.96*lamsq));
   //printf("lam%%: %8.2lf\n",100*unlogit(lm));

   meanx /= SIZE;
   for (k=0;k<SIZE;k++) varx += (x[k]-meanx)*(x[k]-meanx);
   stdevx = sqrt(varx / (SIZE-1));
   //printf("1-ROCA%%: %0.4lf (%0.4lf - %0.4lf)\n",100*unlogit(roca), 100*unlogit(roca-1.96*stdevx), 100*unlogit(roca+1.96*stdevx));
   printf("1-ROCA%%: %0.2lf\n",100*unlogit(roca));
}
