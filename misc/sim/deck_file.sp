* Complete deck for two_stage_opamp circuit with measures and AC analysis

.prot
.lib './include/saed32nm.lib' TT
.unprot

.subckt two_stage_opamp inm inp out vdd vss
xm13 net23 net23 vdd vdd p25 w = 0.9166019920216946u l=0.03u nf = 8 m=1
xm16 out   net22 vdd vdd p25 w=0.33596445561301136u l=0.03u nf=4 m=1
xm15 net41 net41 vdd vdd p25 w=1.602655150938394u l=0.03u nf=7 m=1
xm14 net22 net23 vdd vdd p25 w=0.8253538032194283u l=0.03u nf=7 m=1
xm12 net41 net41 vss vss n25 w=1.3053678038515748u l=0.03u nf=8 m=1
xm10 net15 net41 vss vss n25 w=1.118528478362639u l=0.03u nf=8 m=1
xm9  net22 inp net15 vss n25 w=1.6604988655492978u l=0.03u nf=8 m=1
xm17 net23 inm net15 vss n25 w=1.615197353375396u l=0.03u nf=7 m=1
xm11 out   net41 vss vss n25 w=1.9999198041425346u l=0.03u nf=3 m=1
c19 net22 net58 c=10f
r18 net58 out  r=100k
.ends two_stage_opamp

.param xvdd = 2.5
.param xvcm = 1.25
.GLOBAL gnd!

xi0 inm inp out vdd vss two_stage_opamp
v9 inp vss dc='xvcm' ac=1
v3 vss gnd! dc=0
v2 vdd gnd! dc='xvdd'
cout out vss c=75f
v1  inm out dc=0

.ac dec 10 100k 100G
.lstb mode=single vsource='v1'
.probe ac lstb(db) lstb(p)

.option measfail=0

.meas ac gain_dc find lstb(db) at 100k
.meas ac phase_margin find lstb(p) when lstb(db)=0
.meas ac gain_margin find lstb(db) when lstb(p)=0
.meas ac gain_bandwidth when lstb(db)=0 fall=1.

.end
