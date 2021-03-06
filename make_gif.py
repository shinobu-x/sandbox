import os

def make_gif(save_dir, iter):                                                                                                                  
    gif_output = os.path.join(save_dir, "anim.gif")                                                                              
    if os.path.exists(gif_output):                                                                                                         
        os.remove(gif_output)                                                                                                              
    cmd = ['ffmpeg', '-framerate', '10', '-pattern_type', 'glob',                                                                          
           '-i', f"{save_dir}/*.png", '-loop', '0', gif_output]                                                                  
    try:                                                                                                                                   
        output = subprocess.check_output(cmd)                                                                                              
    except subprocess.CalledProcessError as cpe:                                                                                           
        output = cpe.output                                                                                                                
        print("Ignoring non-zero exit: ", output)                                                                                          
                                                                                                                                           
    return gif_output                                                                                                                      
                                                                                                                                           
# !ffmpeg \                                                                                                                                
#   -framerate 10 -pattern_type glob \                                                                                                     
#   -i '{animation_output}/*_*.png' \                                                                                                      
#   -loop 0 {animation_output}/final.gif
