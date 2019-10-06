x = 0:0.01:3;
hf = figure ();
plot (x, erf (x));
hold on;
plot (x, x, "r");
axis ([0, 3, 0, 1]);
text (0.65, 0.6175, ['$\displaystyle\leftarrow x = {2 \over \sqrt{\pi}}'...
                     '\int_{0}^{x} e^{-t^2} dt = 0.6175$'],
      "interpreter", "latex");
xlabel ("x");
ylabel ("erf (x)");
title ("erf (x) with text annotation");
print (hf, "plot15_7.pdf", "-dpdflatexstandalone");
#system ("pdflatex plot15_7");
#open plot15_7.pdf
