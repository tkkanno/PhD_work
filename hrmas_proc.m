addpath('/home/louic/Desktop/mvapack');
%icoshift data make sure to make ppm a separate file
%add directory where files are
directory = "/home/louic/Desktop/SIMON_TOKUWA/Cell_culture/comparison/TK_UT_Ctr/";
%load spectra and ppm files
spectra  = load(strcat(directory, "raw_spect"));
ppm = load(strcat(directory, "ppm"));

segments = [0.82 1.10; 1.14 1.23; 1.23 1.40; 1.45 1.54; 1.54 1.64;...
	    1.64 1.80; 1.80 2.00; 2.00 2.20; 2.20 2.30; 2.32 2.41;...
	    2.41 2.50; 2.50 2.60; 2.60 2.70; 2.70 2.80; 2.90 3.10;...
	    3.10 3.40; 3.40 3.50; 3.50 3.70; 3.70 3.83; 3.83 4.04;...
	    4.04 4.10; 6.80 7.00; 7.10 7.30;...
	    7.30 7.40; 7.40 7.50; 7.50 7.60; 7.80 7.90; 8.10 8.24];

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