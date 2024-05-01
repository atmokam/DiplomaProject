* Complete deck for two_stage_opamp circuit with measures and AC analysis

.prot
.lib './include/saed32nm.lib' TT
.unprot

.subckt two_stage_opamp inm inp out vdd vss
xm13 net23 net23 vdd vdd p25 w = 0.3u l=0.44u nf = 5 m=1
xm16 out   net22 vdd vdd p25 w=0.3u l=0.44u nf=5 m=1
xm15 net41 net41 vdd vdd p25 w=0.32u l=0.42u nf=1 m=1
xm14 net22 net23 vdd vdd p25 w=0.32u l=0.42u nf=3 m=1
xm12 net41 net41 vss vss n25 w=0.32u l=0.55u nf=1 m=1
xm10 net15 net41 vss vss n25 w=0.67u l=0.42u nf=1 m=1
xm9  net22 inp net15 vss n25 w=0.32u l=0.42u nf=1 m=1
xm17 net23 inm net15 vss n25 w=0.32u l=0.42u nf=1 m=1
xm11 out   net41 vss vss n25 w=0.86u l=1.03u nf=1 m=1
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
