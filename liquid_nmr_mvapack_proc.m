addpath('/home/louic/Desktop/mvapack');
%icoshift data make sure to make ppm a separate file
%add directory where files are
directory = "/home/louic/Desktop/media_nmr/20161004_media/tgf_samples/";
%load spectra and ppm files
spectra  = load(strcat(directory, "raw_spect"));
ppm = spectra(1,:);
spectra = spectra(2:end, :);

segments = [0.88 1.06; 1.06 1.15; 1.15 1.22; 1.22 1.30; 1.30 1.40; 1.41 1.45; 1.45 1.52;... 
	    1.55 1.60; 1.62 1.80; 1.85 1.95; 1.95 2.00; 2.00 2.09; 2.09 2.20;...
	    2.20 2.31; 2.31 2.33; 2.33 2.37; 2.39;2.39 2.416; 2.416 2.492; 2.492 2.54;...
	     2.54 2.56; 2.56 2.60; 2.60 2.70;2.88 2.95; 3.00 3.07; 3.07 3.17;...
	    3.17 3.22; 3.22 3.29; 3.29 3.38; 3.38 3.44; 3.44 3.52; 3.52 3.59;...
	    3.59 3.62; 3.62 3.70; 3.70 3.77; 3.77 3.805;...
	    3.805 3.87; 3.87 3.924; 3.924 3.977; 3.977 4.02; 4.02 4.05; 4.05 4.09;...
	    4.09 4.16; 4.16 4.20; 4.20 4.27; 4.30 4.38; 4.38 4.43; 4.43 4.47; 4.47 4.55;...
	    4.44 4.69; 5.21 5.28; 5.258 5.33; 5.33 5.40;5.40 5.456; 5.456 5.48; 5.48 5.60; ...
	    6.50 6.55; 6.85 6.94; 6.94 7.00; 7.00 7.06;7.15 7.22; 7.28 7.47; 7.50 7.62; ...
	    7.62 7.70; 7.70 7.77; 7.77 7.80; 8.00 8.15;...
	    8.16 8.21; 8.21 8.30; 8.40 8.60; 8.60 8.80; 8.80 8.97];

%exectution 
%global then segmented
shifted = icoshift(spectra, ppm, segments, cofirst =true);
%optimal binning of spectra if desired
[xnew, abnew]=binoptim(shifted, ppm, 0.005);

%merge ppm and data and save
ppm_bin = strcat(directory, "ppm_bin");
bin_shift_data = strcat(directory, "bin_shift_data");

shifted = [ppm;shifted];
abnew = transpose(abnew);
xnew = [abnew;xnew];

save("-text", bin_shift_data, "xnew");

%if you didnt bin then save the shifted spectra
shifted_data = strcat(directory, "shifted_data");
save("-text", shifted_data, "shifted");
