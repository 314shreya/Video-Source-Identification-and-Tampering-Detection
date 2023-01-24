
%filename= 'dataset/2.mp4';
%[nFrames,a]= filetemp(filename);
function [nFrames,a]= filetemp(filename)
    %........................................... TAMPER DETECTION ...............................%

    %......... Reading Video into vid Object .........%
    obj = VideoReader(filename);
    image = read(obj, 1);

    binarization_threshold = 10;
    nFrames = obj.NumberOfFrames;
    nFrames
    rate = obj.FrameRate;
    rate
    %figure, imshow (image);

    %........ Morphological Operation on Image .......%
    image = rgb2gray(image);
    [x y] = size(image);
    [~, threshold] = edge(image, 'sobel');
    fudgeFactor = .8;
    image = edge(image,'sobel', threshold * fudgeFactor);
    %figure, imshow (image);
    %image = edge (image, 'sobel');
    se = strel('line',11,90);
    im2 = imdilate(image, se);
    %figure, imshow (im2);
    %imshow (im2);



    %........ Taking complement of the Image ................%
    countin =0;
    countout = 0;
    ind = 0;
    a = zeros (1, nFrames - 2);
    for i = 1:x
            for j = 1:y
                im2(i,j) = 1- im2(i,j);
            end
    end
    maxTillNow = 0;


    %........ Processing Images for Tamper Detection ........%
    for t = 2:1:nFrames - 1

        countin =0;
        countout = 0;
        n = 0;
        nMinusOne = 0;
        im = read (obj, t);
        %[x, y] = size(image)
        im = rgb2gray(im);


        [~, threshold] = edge(im, 'sobel');
        fudgeFactor = .8;
        im = edge(im,'sobel', threshold * fudgeFactor);
        se = strel('line',11,90);
        im = imdilate(im, se);
        %figure,imshow (im);

        for i = 1:x
            for j = 1:y
                im(i,j) = 1 - im(i,j);

                if (im2(i, j) == 1 && im(i,j) == 0)
                    countout = countout + 1;
                end
                if (im2(i,j) == 0 && im(i, j) == 1)
                    countin = countin + 1;
                end

            end
        end

        if (mod (t,5) == 0)
        %figure,imshow (im);
        end
        %countout
        %countin
        im2 = im;

        %c = min (countout, countin);
        c = countout - countin;
        if (c < 0)
            c = -c;
        end
        ind = ind + 1;
        a(ind) = c;
    end

    maxTillNow

    %........... Final Plot to show Difference ..............%
    xc = [1:nFrames - 2];
    plot (xc,a);
    ylim ([0, 90000]);
end



