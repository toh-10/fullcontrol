default_initial_settings = {
    "name": "Biqu BX",
    "manufacturer": "Biqu",
    "start_gcode": "; BIQU BX Start G-code
    "end_gcode": "                               ;BIQU Default End Gcode\nG91                            ;Relative positioning\nG1 E-2 F2700                   ;Retract a bit\nG1 E-2 Z0.2 F2400              ;Retract a bit more and raise Z\nG1 X5 Y5 F3000                 ;Wipe out\nG1 Z10                         ;Raise Z by 10mm\nG90                            ;Return to absolute positioning\n\nG1 X0 Y{data['build_volume_y']}         ;TaDaaaa\nM106 S0                        ;Turn-off fan\nM104 S0                        ;Turn-off hotend\nM140 S0                        ;Turn-off bed\n\nM84 X Y E                      ;Disable all steppers but Z\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 50,
    "travel_speed": 150.0,
    "dia_feed": 1.75,
    "build_volume_x": 250,
    "build_volume_y": 250,
    "build_volume_z": 250,
}