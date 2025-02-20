#ifndef _PRMT_BLINKQOSTYPE_HG_H_
#define _PRMT_BLINKQOSTYPE_HG_H_


extern struct CWMP_LEAF tBlinkQosTypeLeaf[];
extern struct CWMP_NODE tBlinkQosTypeObject[];
int setBlinkQosType(char *name, struct CWMP_LEAF *entity, int type, void *data);
int getBlinkQosType(char *name, struct CWMP_LEAF *entity, int *type, void **data);
int ObjBlinkQosType(char *name, struct CWMP_LEAF *e, int type, void *data);


#endif
