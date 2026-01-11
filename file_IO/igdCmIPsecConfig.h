#ifndef _IGD_CM_IPSECCONFIG_PUB_H_
#define _IGD_CM_IPSECCONFIG_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>

#define IGD_IPSECCONFIG_TAB  (IGD_DEVICE_TAB_START + 4500)
#define IPSECCONFIG_MAX 16


typedef struct
{
	uword32 ulStateAndIndex;
	uword32 ulIndex;

	word8 Name[128];
#define IPSECCONFIG_ATTR_MASK_BIT0_NAME (1<<0)
	uword8 Enable;
#define IPSECCONFIG_ATTR_MASK_BIT1_ENABLE (1<<1)
	word8 IPSecType[128];
#define IPSECCONFIG_ATTR_MASK_BIT2_IPSECTYPE (1<<2)
	word8 RemoteSubnet[128];
#define IPSECCONFIG_ATTR_MASK_BIT3_REMOTESUBNET (1<<3)
	word8 LocalSubnet[128];
#define IPSECCONFIG_ATTR_MASK_BIT4_LOCALSUBNET (1<<4)
	word8 RemoteIP[128];
#define IPSECCONFIG_ATTR_MASK_BIT5_REMOTEIP (1<<5)
	word8 RemoteDomain[128];
#define IPSECCONFIG_ATTR_MASK_BIT6_REMOTEDOMAIN (1<<6)
	word8 ExchangeMode[128];
#define IPSECCONFIG_ATTR_MASK_BIT7_EXCHANGEMODE (1<<7)
	word8 IKEAuthenticationAlgorithm[128];
#define IPSECCONFIG_ATTR_MASK_BIT8_IKEAUTHENTICATIONALGORITHM (1<<8)
	word8 IKEAuthenticationMethod[128];
#define IPSECCONFIG_ATTR_MASK_BIT9_IKEAUTHENTICATIONMETHOD (1<<9)
	word8 IKEEncryptionAlgorithm[128];
#define IPSECCONFIG_ATTR_MASK_BIT10_IKEENCRYPTIONALGORITHM (1<<10)
	word8 IKEDHGroup[128];
#define IPSECCONFIG_ATTR_MASK_BIT11_IKEDHGROUP (1<<11)
	word8 IKEIDType[128];
#define IPSECCONFIG_ATTR_MASK_BIT12_IKEIDTYPE (1<<12)
	word8 IKELocalName[128];
#define IPSECCONFIG_ATTR_MASK_BIT13_IKELOCALNAME (1<<13)
	word8 IKERemoteName[128];
#define IPSECCONFIG_ATTR_MASK_BIT14_IKEREMOTENAME (1<<14)
	word8 IKEPreshareKey[128];
#define IPSECCONFIG_ATTR_MASK_BIT15_IKEPRESHAREKEY (1<<15)
	word8 IPSecOutInterface[128];
#define IPSECCONFIG_ATTR_MASK_BIT16_IPSECOUTINTERFACE (1<<16)
	word8 IPSecEncapsulationMode[128];
#define IPSECCONFIG_ATTR_MASK_BIT17_IPSECENCAPSULATIONMODE (1<<17)
	word8 IPSecTransform[128];
#define IPSECCONFIG_ATTR_MASK_BIT18_IPSECTRANSFORM (1<<18)
	word8 ESPAuthenticationAlgorithm[128];
#define IPSECCONFIG_ATTR_MASK_BIT19_ESPAUTHENTICATIONALGORITHM (1<<19)
	word8 ESPEncryptionAlgorithm[128];
#define IPSECCONFIG_ATTR_MASK_BIT20_ESPENCRYPTIONALGORITHM (1<<20)
	word8 IPSecPFS[128];
#define IPSECCONFIG_ATTR_MASK_BIT21_IPSECPFS (1<<21)
	uword32 IKESAPeriod;
#define IPSECCONFIG_ATTR_MASK_BIT22_IKESAPERIOD (1<<22)
	uword32 IPSecSATimePeriod;
#define IPSECCONFIG_ATTR_MASK_BIT23_IPSECSATIMEPERIOD (1<<23)
	uword32 IPSecSATrafficPeriod;
#define IPSECCONFIG_ATTR_MASK_BIT24_IPSECSATRAFFICPERIOD (1<<24)
	word8 AHAuthenticationAlgorithm[128];
#define IPSECCONFIG_ATTR_MASK_BIT25_AHAUTHENTICATIONALGORITHM (1<<25)
	uword8 DPDEnable;
#define IPSECCONFIG_ATTR_MASK_BIT26_DPDENABLE (1<<26)
	uword32 DPDThreshold;
#define IPSECCONFIG_ATTR_MASK_BIT27_DPDTHRESHOLD (1<<27)
	uword32 DPDRetry;
#define IPSECCONFIG_ATTR_MASK_BIT28_DPDRETRY (1<<28)
	word8 ConnectionStatus[128];
#define IPSECCONFIG_ATTR_MASK_BIT29_CONNECTIONSTATUS (1<<29)
#define QOS_LIST_ATTR_MASK_ALL (0xfff)
	uword32 ulBitmap;
} __PACK__ IgdIPsecConfigTab;


word32 igdCmIPsecConfigAdd(uword8 *pucInfo, uword32 len);
word32 igdCmIPsecConfigDel(uword8 *pucInfo, uword32 len);
word32 igdCmIPsecConfigGet(uword8 *pucInfo, uword32 len);
word32 igdCmIPsecConfigSet(uword8 *pucInfo, uword32 len);
word32 igdCmIPsecConfigGetNum(uword32 *entrynum);
word32 igdCmIPsecConfigGetAllIndex(uword8 *pucInfo, uword32 len);
word32 igdCmIPsecConfigGetAllInfo(uword8 *pucInfo, uword32 len);
word32 igdCmIPsecConfigInit(void);



IGDCM_OPER_REG(IGD_IPSECCONFIG_TAB, igdCmIPsecConfigAdd, igdCmIPsecConfigDel,igdCmIPsecConfigSet, igdCmIPsecConfigGet, igdCmIPsecConfigGetNum, igdCmIPsecConfigGetAllIndex, igdCmIPsecConfigGetAllInfo, 0, 0, 0);
#endif

IgdIPsecConfigTab *em_IPsecConfig_entry = 0;
XML_DIR_ARRAY( root, em_IPsecConfig_entry, "EM_IPSECCONFIG_TAB", 16, IGD_IPSECCONFIG_TAB);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, ulIndex);
XML_ENTRY_STRING2(em_IPsecConfig_entry, Name);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, Enable);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IPSecType);
XML_ENTRY_STRING2(em_IPsecConfig_entry, RemoteSubnet);
XML_ENTRY_STRING2(em_IPsecConfig_entry, LocalSubnet);
XML_ENTRY_STRING2(em_IPsecConfig_entry, RemoteIP);
XML_ENTRY_STRING2(em_IPsecConfig_entry, RemoteDomain);
XML_ENTRY_STRING2(em_IPsecConfig_entry, ExchangeMode);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKEAuthenticationAlgorithm);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKEAuthenticationMethod);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKEEncryptionAlgorithm);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKEDHGroup);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKEIDType);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKELocalName);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKERemoteName);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IKEPreshareKey);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IPSecOutInterface);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IPSecEncapsulationMode);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IPSecTransform);
XML_ENTRY_STRING2(em_IPsecConfig_entry, ESPAuthenticationAlgorithm);
XML_ENTRY_STRING2(em_IPsecConfig_entry, ESPEncryptionAlgorithm);
XML_ENTRY_STRING2(em_IPsecConfig_entry, IPSecPFS);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, IKESAPeriod);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, IPSecSATimePeriod);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, IPSecSATrafficPeriod);
XML_ENTRY_STRING2(em_IPsecConfig_entry, AHAuthenticationAlgorithm);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, DPDEnable);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, DPDThreshold);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, DPDRetry);
XML_ENTRY_STRING2(em_IPsecConfig_entry, ConnectionStatus);
XML_ENTRY_PRIMITIVE2(em_IPsecConfig_entry, ulBitmap);
