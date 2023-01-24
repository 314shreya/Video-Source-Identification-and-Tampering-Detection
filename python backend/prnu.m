function[] = prnu()

% estimate PRNU from images in prnu/*
d = dir( 'prnu/*.tif' );
N = numel(d);
num = [];
den = [];
for k = 1 : N-1 % estimate from all but last image
    fprintf( 'processing %d/%d\n', k, numel(d) );
    f = imread( sprintf( 'prnu/%s', d(k).name ) ); % load image
    [num,den,K] = estimatePRNU( f, num, den );
end

% correlate PRNU to last image and flipped version of last image
f = imread( sprintf( 'prnu/%s', d(N).name ) ); % load image
[~,~,k1] = estimatePRNU( f, [], [] ); % this should have a high correlation
[~,~,k2] = estimatePRNU( fliplr(f), [], [] ); % this flipped image should have a low correlation
fprintf('%f',k1)

fprintf( '%f %f\n', corr2(K,k1), corr2(K,k2) );


% -----------------------------------------
function[num,den,k] = estimatePRNU(f,num,den)
f = double( rgb2gray(f) );
g = wiener2( f ); % denoise
if( isempty(num) ) % initialize
    [ydim,xdim,zdim] = size(f);
    num = zeros( ydim, xdim, zdim );
    den = zeros( ydim, xdim, zdim );
end
num = num + (g .* (f - g));
den = den + (g .^ 2);
k = num ./ den;
