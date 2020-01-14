import probvis.aux as pva
import probvis.distributions.lognormal as pvln

pva.activate_latex_format()

save_dir = 'images'

pvln.plot_pdf(save_dir=save_dir, mean=0.4, sigma=0.1)
pvln.plot_pdf(save_dir=save_dir, mean=0.4, sigma=1)


pvln.plot_pdf(save_dir=save_dir, mean=1, sigma=0.1)
pvln.plot_pdf(save_dir=save_dir, mean=1, sigma=1)

pvln.plot_pdf(save_dir=save_dir, mean=3, sigma=0.1)
pvln.plot_pdf(save_dir=save_dir, mean=3, sigma=1)
