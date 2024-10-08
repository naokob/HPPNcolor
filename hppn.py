from pymol import cmd

def hppn(selection="all"):
    # PyMOL commands for basic display settings
    cmd.set("valence", 0)
    cmd.set("cartoon_gap_cutoff", 0)
    cmd.set("ray_opaque_background", "off")
    cmd.set("ray_shadow", "off")
    cmd.set("depth_cue", 0)
    cmd.set("spec_reflect", 0.2)
    cmd.set("cartoon_discrete_colors", "on")
    cmd.hide("all")
    cmd.show("cartoon", selection)
    cmd.color("white", selection)
    cmd.set("cartoon_smooth_loops", 0)
    cmd.set("cartoon_flat_sheets", 0)
    cmd.set("cartoon_oval_length", 1.5)
    cmd.set("cartoon_oval_width", 0.5)
    cmd.set("cartoon_rect_length", 1.8)
    cmd.set("cartoon_rect_width", 0.58)
    cmd.set("cartoon_loop_radius", 0.5)
    cmd.set("stick_radius", 0.4)
    cmd.set("dash_width", 4)
    cmd.set("dash_color", "aquamarine")
    cmd.set("stick_h_scale", 1)

    # Selections based on residue type
    cmd.select("hydrophobes", "(resn val+ile+leu+phe+tyr+trp+met)")
    cmd.select("polar", "(resn asn+gln+ser+thr)")
    cmd.select("positive", "(resn his+lys+arg)")
    cmd.select("negative", "(resn asp+glu)")
    cmd.select("Gs", "(resn gly)")
    cmd.select("Ps", "(resn pro)")
    cmd.select("As", "(resn ala)")
    cmd.select("Cs", "(resn cys)")

    # Coloring the selections
    cmd.color("tv_yellow", "hydrophobes")
    cmd.color("cyan", "polar")
    cmd.color("tv_blue", "positive")
    cmd.color("tv_red", "negative")
    cmd.color("tv_green", "Gs")
    cmd.color("tv_orange", "Ps")
    cmd.color("white", "As")
    cmd.color("limon", "Cs")

    # Show sticks for specific atoms in the selections
    cmd.show("sticks", "(hydrophobes and (!name c+n+o))")
    cmd.show("sticks", "(polar and (!name c+n+o))")
    cmd.show("sticks", "(positive and (!name c+n+o))")
    cmd.show("sticks", "(negative and (!name c+n+o))")
    cmd.show("sticks", "(Gs and (!name c+n+o))")
    cmd.show("sticks", "(Ps and (!name c+o))")
    cmd.show("sticks", "(As and (!name c+n+o))")
    cmd.show("sticks", "(Cs and (!name c+n+o))")

    # Hide hydrogens and disable selections
    cmd.hide("(hydro)")
    cmd.disable("hydrophobes")
    cmd.disable("polar")
    cmd.disable("positive")
    cmd.disable("negative")
    cmd.disable("Gs")
    cmd.disable("Ps")
    cmd.disable("As")
    cmd.disable("Cs")

    # Set cartoon colors for specific selections
    cmd.set("cartoon_color", "white")
    cmd.set("cartoon_color", "tv_green", "Gs")

def uncc(selection="all"):
    # PyMOL commands for unset cartoon_color
    cmd.unset("cartoon_color")
    cmd.unset("cartoon_color", "(all)")
 
# Extend the command to be usable in PyMOL
cmd.extend("hppn", hppn)
cmd.extend("uncc", uncc)
