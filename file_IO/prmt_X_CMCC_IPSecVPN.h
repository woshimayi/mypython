#ifndef _PRMT_IPSECVPN_HG_H_
#define _PRMT_IPSECVPN_HG_H_


extern struct CWMP_LEAF tIpSecVpnLeaf[];
extern struct CWMP_NODE tIpSecVpnObject[];
int setIpSecVpn(char *name, struct CWMP_LEAF *entity, int type, void *data);
int getIpSecVpn(char *name, struct CWMP_LEAF *entity, int *type, void **data);
#endif
