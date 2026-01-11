#ifndef _PRMT_IPSECCONFIG_HG_H_
#define _PRMT_IPSECCONFIG_HG_H_


extern struct CWMP_LEAF tIPsecConfigLeaf[];
extern struct CWMP_NODE tIPsecConfigObject[];
int setIPsecConfig(char *name, struct CWMP_LEAF *entity, int type, void *data);
int getIPsecConfig(char *name, struct CWMP_LEAF *entity, int *type, void **data);
int ObjIPsecConfig(char *name, struct CWMP_LEAF *e, int type, void *data);


#endif
