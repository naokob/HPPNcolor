set valence, 0
set cartoon_gap_cutoff, 0
set ray_opaque_background, off
set ray_shadow, off
set depth_cue, 0
set spec_reflect, 0.2
set cartoon_discrete_colors, on
hide all
show cartoon, all
color white, all
set cartoon_smooth_loops, 0
set cartoon_flat_sheets, 0
set cartoon_oval_length, 1.5
set cartoon_oval_width, 0.5
set cartoon_rect_length, 1.8
set cartoon_rect_width, 0.58
set cartoon_loop_radius, 0.5
set stick_radius, 0.4
set dash_width, 4
set dash_color, aquamarine
set stick_h_scale, 1
select hydrophobes, (resn val+ile+leu+phe+tyr+trp+met)
select polar, (resn asn+gln+ser+thr)
select positive, (resn his+lys+arg)
select negative, (resn asp+glu)
select Gs, (resn gly)
select Ps, (resn pro)
select As, (resn ala)
select Cs, (resn cys)
color tv_yellow, hydrophobes
color cyan, polar
color tv_blue, positive
color tv_red, negative
color tv_green, Gs
color tv_orange, Ps
color white, As
color limon, Cs
show sticks, (hydrophobes and (!name c+n+o))
show sticks, (polar and (!name c+n+o))
show sticks, (positive and (!name c+n+o))
show sticks, (negative and (!name c+n+o))
show sticks, (Gs and (!name c+n+o))
show sticks, (Ps and (!name c+o))
show sticks, (As and (!name c+n+o))
show sticks, (Cs and (!name c+n+o))
hide (hydro)
disable hydrophobes
disable polar
disable positive
disable negative
disable Gs
disable Ps
disable As
disable Cs
color white, name ca
color tv_green, name ca and Gs
#set cartoon_color, white
#set cartoon_color, tv_green, Gs
