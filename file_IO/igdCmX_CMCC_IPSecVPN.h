#ifndef _IGD_CM_IPSECVPN_PUB_H_
#define _IGD_CM_IPSECVPN_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>

#define IGD_IPSECVPN_TAB  (IGD_DEVICE_TAB_START + )
#define IPSECVPN_MAX 16


typedef struct
{
	uword32 ulStateAndIndex;
	uword32 ulIndex;

	uword32 MaxNumberOfEntries;
#define IPSECVPN_ATTR_MASK_BIT0_MAXNUMBEROFENTRIES (1<<0)
	uword32 IPSecVPNNumberOfEntries;
#define IPSECVPN_ATTR_MASK_BIT1_IPSECVPNNUMBEROFENTRIES (1<<1)
#define QOS_LIST_ATTR_MASK_ALL (0xfff)
	uword32 ulBitmap;
} __PACK__ IgdIpSecVpnTab;


word32 igdCmIpSecVpnGet(uword8 *pucInfo, uword32 len);
word32 igdCmIpSecVpnSet(uword8 *pucInfo, uword32 len);
word32 igdCmIpSecVpnInit(void);



IGDCM_OPER_REG(IGD_IPSECVPN_TAB, 0,  0, igdCmIpSecVpnSet, igdCmIpSecVpnGet, 0,  0,  0,  0, 0, 0);
#endif

IgdIpSecVpnTab *em_IpSecVpn_entry = 0;
XML_DIR_ARRAY( root, em_IpSecVpn_entry, "EM_IPSECVPN_TAB", 16, IGD_IPSECVPN_TAB);
XML_ENTRY_PRIMITIVE2(em_IpSecVpn_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_IpSecVpn_entry, ulIndex);
XML_ENTRY_PRIMITIVE2(em_IpSecVpn_entry, MaxNumberOfEntries);
XML_ENTRY_PRIMITIVE2(em_IpSecVpn_entry, IPSecVPNNumberOfEntries);
XML_ENTRY_PRIMITIVE2(em_IpSecVpn_entry, ulBitmap);
