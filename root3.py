from geometor import *

sp.init_printing()

BUILD = True
ANALYZE = False

PART1 = True
PART2 = False
PART3 = False
PART4 = False

def main():
    if PART1:
        print_log(f'\nPART1')
        if PART2:
            print_log('PART2')
            if PART3:
                print_log('PART3')
                if PART4:
                    print_log('PART4')

    NAME = 'root3-'
    NAME += input(f'\nsession name: {NAME}')
    log_init(NAME)

    start_time = timer()

    print_log(f'\nMODEL: {NAME}')

    # add starting points
    start_time = timer()

    M = Model()
    # TODO: add label to Models
    A = M.gen_point(0, 0, classes=['start'])
    B = M.gen_point(1, 0, classes=['start'])
    baseline = M.gen_line(A, B)

    c1 = M.gen_circle(A, B)
    C = M.points()[-1]

    c2 = M.gen_circle(B, A)
    D = M.points()[-3]
    E = M.points()[-2]
    F = M.points()[-1]

    t1 = M.gen_polygon([A, B, E])
    t2 = M.gen_polygon([A, B, F])

    len_pts = len(M.points())
    bisector = M.gen_line(E, F, classes=['bisector'])

    O = M.points()[len_pts]

    len_pts = len(M.points())
    l = M.gen_line(A, E)
    G = M.points()[len_pts]

    len_pts = len(M.points())
    l = M.gen_line(B, E)
    H = M.points()[len_pts]

    t3 = M.gen_polygon([G, E, H])
    
    l = M.gen_line(A, F)

    l = M.gen_line(B, F)

    M.summary()

    print_log(f'\nANALYZE: {NAME}')
    sections, sections_by_line = analyze_golden(M)


    # PLOT *********************************
    print_log(f'\nPLOT: {NAME}')

    fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
    plt.tight_layout()

    plot_model(NAME, ax, ax_btm, M)

    #  title = f'G E O M E T O R'
    #  fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

    print_log('\nPlot Goldens')
    plot_sections(NAME, ax, ax_btm, sections)

    plot_all_sections(NAME, ax, ax_btm, M, sections)

    print_log('\nPlot Golden Groups')
    groups = group_sections(sections)
    plot_all_groups(NAME, ax, ax_btm, M, groups)

    #  add_element(line(D, C, classes=['bisector']))
    #  add_element(line(A, pts[9], classes=['bisector']))
    #  add_element(line(B, pts[6], classes=['bisector']))
    #  circumcenter = pts[14]

    #  # circumcircle
    #  add_element(circle(circumcenter, D, classes=['gold']))

    #  add_element(circle(C, A))
    #  add_element(line(pts[6], pts[9]))

    #  if PART1:
        #  nine_ids = [4, 22, 19, 9, 21, 23, 6, 18, 20]
        #  nine = add_polygon(polygon_ids(nine_ids, classes=['nine']))

        #  add_element(line(pts[20], pts[22], classes=['red']))
        #  add_element(line(pts[19], pts[21], classes=['red']))
        #  add_element(line(pts[23], pts[18], classes=['red']))

        #  if PART2:
            #  pt_apex = D
            #  add_element(line(pt_apex, pts[22], classes=['green']))
            #  if PART3:
                #  add_element(line(pt_apex, pts[19], classes=['set1']))
                #  if PART4:
                    #  add_element(line(pt_apex, pts[21], classes=['set2']))
                    #  add_element(line(pt_apex, pts[23], classes=['set2']))
                #  add_element(line(pt_apex, pts[18], classes=['set1']))
            #  add_element(line(pt_apex, pts[20], classes=['green']))

            #  pt_apex = pts[6]
            #  add_element(line(pt_apex, pts[18], classes=['green']))
            #  if PART3:
                #  add_element(line(pt_apex, pts[20], classes=['set1']))
                #  if PART4:
                    #  add_element(line(pt_apex, pts[22], classes=['set2']))
                    #  add_element(line(pt_apex, pts[19], classes=['set2']))
                #  add_element(line(pt_apex, pts[21], classes=['set1']))
            #  add_element(line(pt_apex, pts[23], classes=['green']))

            #  pt_apex = pts[9]
            #  add_element(line(pt_apex, pts[21], classes=['green']))
            #  if PART3:
                #  add_element(line(pt_apex, pts[23], classes=['set1']))
                #  if PART4:
                    #  add_element(line(pt_apex, pts[18], classes=['set2']))
                    #  add_element(line(pt_apex, pts[20], classes=['set2']))
                #  add_element(line(pt_apex, pts[22], classes=['set1']))
            #  add_element(line(pt_apex, pts[19], classes=['green']))

    #  model_summary(NAME, start_time)

    #  # ANALYZE ***************************
    #  if ANALYZE:
        #  print_log(f'\nANALYZE: {NAME}')
        #  goldens, groups = analyze_model()

        #  analyze_summary(NAME, start_time, goldens, groups)

    #  # PLOT *********************************
    #  print_log(f'\nPLOT: {NAME}')
    #  limx, limy = get_limits_from_points(pts, margin=.25)
    #  limx, limy = adjust_lims(limx, limy)
    #  bounds = set_bounds(limx, limy)
    #  print_log()
    #  print_log(f'limx: {limx}')
    #  print_log(f'limy: {limy}')

    #  #  plt.ion()
    #  fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
    #  ax_btm.axis('off')
    #  ax.axis('off')
    #  ax.set_aspect('equal')
    #  plt.tight_layout()

    #  title = f'G E O M E T O R'
    #  fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

    #  print_log('\nPlot Summary')
    #  xlabel = f'elements: {len(elements)} | points: {len(pts)}'
    #  ax_prep(ax, ax_btm, bounds, xlabel)
    #  plot_sequence(ax, history, bounds)
    #  snapshot(NAME, 'sequences/summary.png')

    #  if BUILD:
        #  print_log('\nPlot Build')
        #  build_sequence(NAME, ax, ax_btm, history, bounds)

    #  if ANALYZE:
        #  print_log('\nPlot Goldens')

        #  bounds = get_bounds_from_sections(goldens)

        #  plot_sections(NAME, ax, ax_btm, history, goldens, bounds)

        #  print_log('\nPlot Golden Groups')
        #  plot_all_groups(NAME, ax, ax_btm, history, groups, bounds)

        #  plot_all_sections(NAME, ax, ax_btm, history, goldens, bounds)

        #  complete_summary(NAME, start_time, goldens, groups)

    #  else:
        #  model_summary(NAME, start_time)

    #  plt.show()

if __name__ == "__main__":
    main()

