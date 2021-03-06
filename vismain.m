% intialising
tree = load('tree2.txt');
prop = load('prop.txt');
start = [prop(1);prop(2)];
robodim = [prop(3),prop(4)];
roboA = prop(5);
arenadim = [prop(6),prop(7)];
doordim = prop(8);
delay = 0.2;
delay2 = 0.1;
% setting up the figure
figure(1)
% creating arena 
arenaC = [-1*arenadim(1)/2, -1*arenadim(2)/2];
arena = createRect(arenaC,arenadim,1);

% robot
robo = createRect(start, robodim, 1);
robo.FaceColor = 'magenta';
% creating door
door  = line([0, -1*doordim(1)],[0,0], 'LineWidth',8,'Color','red');

%intial arm pos
anglei = [pi;-pi/2];
doori = [start(1) + roboA;start(2);1];
%aset = jangle([start;1],[start;1],doori,[-1*doordim;0;1],[0;0],roboA);
aset = getanagle([start;1],[start;1],doori,[-1*doordim;0;1],[0;0],roboA);
nangle = aset(:,end);
X = forward2(nangle,roboA);
Pos = [X(1,1) + start(1),X(1,2) + start(1); X(2,1) + start(2),X(2,2) + start(2)];

%create the arm
link1 = line([start(1), Pos(1,1)], [start(2),Pos(2,1)],'LineWidth',4,'Color','blue');
% create the arm2
link2 = line([ Pos(1,1),Pos(1,2)], [Pos(2,1),Pos(2,2)],'LineWidth',4,'Color','blue');

pause();

% moving door 
initDoorangle = atan2(start(2)+robodim(2)/2, start(1)-robodim(1)/2);
angle = -pi;
angleiter = 0.1;
pause(delay2)
while abs(angle - initDoorangle) > 0.05
    angle = angle + angleiter;
    x = [0, -1*(abs(doordim*cos(angle)))];
    y = [0,-1*abs(doordim*sin(angle))];
    door.XData = x;
    door.YData = y;
    
    % updating the links
    %aset = jangle([start;1],[start;1],[doori;1],[x(2);y(2);1],[0;0],roboA);
    aset = getanagle([start;1],[start;1],[doori;1],[x(2);y(2);1],[0;0],roboA);
    nangle = aset(:,end);
    X = forward2(nangle,roboA);
    Pos = [X(1,1) + start(1),X(1,2) + start(1); X(2,1) + start(2),X(2,2) + start(2)];
    link1.XData = [start(1),Pos(1,1)];
    link1.YData = [start(2),Pos(2,1)];
    
    link2.XData = [ Pos(1,1),Pos(1,2)];
    link2.YData = [Pos(2,1),Pos(2,2)];
    
    doori = [x(2);y(2)];
    pause(delay2);
 
end
doorpre = [-doordim;0];
display('now the fmincon starts')

for i  = 1:size(tree,1)
    % updating robo positions
   robopos = tree(i,1:2);
   robo.Position = [robopos(1) - robodim(1)/2, robopos(2) - robodim(2)/2, robodim(1), robodim(2)];
   
   % updating door position
   
   dangle = doorangle(tree(i,:), robodim);
   x = [0,doordim*cos(dangle)];
   y = [0,doordim*sin(dangle)];
   door.XData = x;
   door.YData =y;
   
%    c1.centers = [robopos(1),robopos(2)];
   
   %updating the manipulator
   if i >1
       %aset = jangle([tree(i-1,1:2)';1],[tree(i,1:2)';1],[doorpre;1],[x(2);y(2);1],nangle,roboA);
       
       
       aset = getanagle([tree(i-1,1:2)';1],[tree(i,1:2)';1],[doorpre;1],[x(2);y(2);1],nangle,roboA);
       if numel(aset) <2
           continue
       end
       nangle = aset(:,end);
       X = forward2(nangle,roboA);
       Pos = [X(1,1) + robopos(1),X(1,2) + robopos(1); X(2,1) + robopos(2),X(2,2) + robopos(2)];
       
       % create the arm
       link1.XData = [robopos(1), Pos(1,1)];
       link1.YData =  [robopos(2),Pos(2,1)];
       % create the arm
       link2.XData = [ Pos(1,1),Pos(1,2)];
       link2.YData =  [Pos(2,1),Pos(2,2)];
   end
   doorpre = [x(2);y(2)];
   pause()
end
