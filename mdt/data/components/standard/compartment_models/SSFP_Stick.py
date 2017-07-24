from mdt.component_templates.compartment_models import CompartmentTemplate


class SSFP_Stick(CompartmentTemplate):

    parameter_list = ('g', 'd', 'theta', 'phi', 'delta', 'G', 'TR', 'flip_angle', 'b1_static', 'T1_static', 'T2_static')
    dependency_list = ('SSFP',)
    cl_code = '''
        mot_float_type adc = d * pown(dot(g, (mot_float_type4)(cos(phi) * sin(theta), sin(phi) * sin(theta),
                                                               cos(theta), 0.0)), 2);

        return SSFP(adc, delta, G, TR, flip_angle, b1_static, T1_static, T2_static);
    '''
