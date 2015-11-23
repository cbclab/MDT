#ifndef DMRICM_ZEPPELIN_H
#define DMRICM_ZEPPELIN_H

/**
 * Author = Robbert Harms
 * Date = 2014-02-26
 * License = LGPL v3
 * Maintainer = Robbert Harms
 * Email = robbert.harms@maastrichtuniversity.nl
 */

 /**
 * Generate the compartment model signal for the Zeppelin model.
 * @params g the protocol gradient vector with (x, y, z)
 * @params b the protocol b
 * @params d the parameter d
 * @params theta the parameter theta
 * @params phi the parameter phi
 * @params dperp the perpendicular diffusivity
 */
MOT_FLOAT_TYPE cmZeppelin(const MOT_FLOAT_TYPE4 g,
                       const MOT_FLOAT_TYPE b,
                       const MOT_FLOAT_TYPE d,
                       const MOT_FLOAT_TYPE dperp,
                       const MOT_FLOAT_TYPE theta,
                       const MOT_FLOAT_TYPE phi);

#endif // DMRICM_ZEPPELIN_H