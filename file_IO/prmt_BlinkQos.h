#ifndef _PRMT_BLINKQOS_HG_H_
#define _PRMT_BLINKQOS_HG_H_


extern struct CWMP_LEAF tBlinkQosLeaf[];
extern struct CWMP_NODE tBlinkQosObject[];
int setBlinkQos(char *name, struct CWMP_LEAF *entity, int type, void *data);
int getBlinkQos(char *name, struct CWMP_LEAF *entity, int *type, void **data);
#endif
