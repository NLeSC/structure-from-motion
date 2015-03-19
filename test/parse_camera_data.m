

clear
close all
clc



theDir = 'SITE_662';

bundleFile = [theDir,filesep,'bundle',filesep,'bundle.out'];

fid = fopen(bundleFile,'rt');

C = textscan(fid,'%d%d',1,'headerlines',1);

nCameras = double(C{1});
nKeyPoints = double(C{2});

nDataPerCamera = 5*3;

C = textscan(fid,'%f',nDataPerCamera*nCameras);

for iCamera = 1:nCameras
    
    idx = (iCamera - 1) * nDataPerCamera;
    
    cameras(iCamera,1).focalLength = C{1}(idx + 1);
    cameras(iCamera,1).radialDistortCoefs = transpose(C{1}(idx + (2:3)));
    cameras(iCamera,1).rotation = transpose(reshape(C{1}(idx + 3 + (1:9)),[3,3]));
    cameras(iCamera,1).translate = transpose(C{1}(idx + 12 + (1:3)));
    
    % derived properties:
    cameras(iCamera,1).position = (-cameras(iCamera,1).rotation' * cameras(iCamera,1).translate')';
    cameras(iCamera,1).viewDir = (cameras(iCamera,1).rotation' * [0,0,-1]')';
    cameras(iCamera,1).up = (cameras(iCamera,1).rotation' * [0,1,0]')';
end

fclose(fid);


formatStrJSON = ['{"srid": 32633,\n',...
            ' "x": %f,\n',...
            ' "y": %f,\n',...
            ' "z": %f,\n',...
            ' "dx": %f,\n',...
            ' "dy": %f,\n',...
            ' "dz": %f,\n',...
            ' "ux": %f,\n',...
            ' "uy": %f,\n',...
            ' "uz": %f,\n',...
            ' }'];


        

formatStr = sprintf('%%0%dd',ceil(log10(nCameras))+1);

listFile = [theDir,filesep,'prepare',filesep,'list.txt'];
fid = fopen(listFile,'rt');
C = textscan(fid,'%s%d%f');
fclose(fid);

filenames = C{1};

for iCamera = 1:nCameras
    
    filename = [filenames{iCamera},'.json'];
    fopen(filename,'wt');
    fprintf(fid,formatStrJSON,cameras(iCamera).position,cameras(iCamera).translate,cameras(iCamera).viewDir);
    fclose(fid);
    
end

%%
viewDirScaleFactor = 5.0;
scale2 = 1;

close all
figure

ups = zeros(nCameras, 3);
positions = zeros(nCameras, 3);
for iCamera = 1:nCameras
    currentcam = cameras(iCamera);
    position = currentcam.position;
    viewDir = currentcam.viewDir;
    translation = currentcam.translate;
    up = currentcam.up
    plot3(position(1),position(2),position(3),'om','markerfacecolor','m')
    hold on
    plot3(position(1) + [0,viewDir(1)*viewDirScaleFactor],...
          position(2) + [0,viewDir(2)*viewDirScaleFactor],...
          position(3) + [0,viewDir(3)*viewDirScaleFactor],...
          '-b')
    plot3(position(1) + [0,up(1)*scale2],...
          position(2) + [0,up(2)*scale2],...
          position(3) + [0,up(3)*scale2],...
          '-g')
    text(position(1),position(2),position(3),num2str(iCamera));  
    ups(iCamera,:) = currentcam.up';
    positions(iCamera,:) = currentcam.position';
        
end
meanpos = mean(positions,1)
meanup = mean(ups,1)
up = meanup / sqrt(meanup * meanup')
upfrompos = up + meanpos
upscale = 2;
plot3(meanpos(1) + [0,up(1)*upscale],...
          meanpos(2) + [0,up(2)*upscale],...
          meanpos(3) + [0,up(3)*upscale],...
          '-r')
      
grid on
%axis image








