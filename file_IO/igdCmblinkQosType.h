#ifndef _IGD_CM_BLINKQOSTYPE_PUB_H_
#define _IGD_CM_BLINKQOSTYPE_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>

#define IGD_BLINKQOSTYPE_TAB  (IGD_DEVICE_TAB_START + 4500)
#define BLINKQOSTYPE_MAX 16


typedef struct
{
	uword32 ulStateAndIndex;
	uword32 ulIndex;

	uword32 QosPriority;
#define BLINKQOSTYPE_ATTR_MASK_BIT0_QOSPRIORITY (1<<0)
	uword8 DscpEnable;
#define BLINKQOSTYPE_ATTR_MASK_BIT1_DSCPENABLE (1<<1)
	uword32 DscpPriority;
#define BLINKQOSTYPE_ATTR_MASK_BIT2_DSCPPRIORITY (1<<2)
	uword8 Vlan8021pEnable;
#define BLINKQOSTYPE_ATTR_MASK_BIT3_VLAN8021PENABLE (1<<3)
	uword32 Vlan8021p;
#define BLINKQOSTYPE_ATTR_MASK_BIT4_VLAN8021P (1<<4)
	word8 SourceIp[32];
#define BLINKQOSTYPE_ATTR_MASK_BIT5_SOURCEIP (1<<5)
	uword32 SourcePort;
#define BLINKQOSTYPE_ATTR_MASK_BIT6_SOURCEPORT (1<<6)
	word8 DestinationIp[128];
#define BLINKQOSTYPE_ATTR_MASK_BIT7_DESTINATIONIP (1<<7)
	uword32 DestinationPort;
#define BLINKQOSTYPE_ATTR_MASK_BIT8_DESTINATIONPORT (1<<8)
	word8 Protocol[64];
#define BLINKQOSTYPE_ATTR_MASK_BIT9_PROTOCOL (1<<9)
	word8 SourceMac[17];
#define BLINKQOSTYPE_ATTR_MASK_BIT10_SOURCEMAC (1<<10)
	word8 DestinationMac[17];
#define BLINKQOSTYPE_ATTR_MASK_BIT11_DESTINATIONMAC (1<<11)
#define QOS_LIST_ATTR_MASK_ALL (0xfff)
	uword32 ulBitmap;
} __PACK__ IgdBlinkQosTypeTab;


word32 igdCmBlinkQosTypeAdd(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosTypeDel(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosTypeGet(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosTypeSet(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosTypeGetNum(uword32 *entrynum);
word32 igdCmBlinkQosTypeGetAllIndex(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosTypeGetAllInfo(uword8 *pucInfo, uword32 len);
word32 igdCmBlinkQosTypeInit(void);



IGDCM_OPER_REG(IGD_BLINKQOSTYPE_TAB, igdCmBlinkQosTypeAdd, igdCmBlinkQosTypeDel,igdCmBlinkQosTypeSet, igdCmBlinkQosTypeGet, igdCmBlinkQosTypeGetNum, igdCmBlinkQosTypeGetAllIndex, igdCmBlinkQosTypeGetAllInfo, 0, 0, 0);
#endif

IgdBlinkQosTypeTab *em_BlinkQosType_entry = 0;
XML_DIR_ARRAY( root, em_BlinkQosType_entry, "EM_BLINKQOSTYPE_TAB", 16, IGD_BLINKQOSTYPE_TAB);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, ulIndex);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, QosPriority);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, DscpEnable);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, DscpPriority);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, Vlan8021pEnable);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, Vlan8021p);
XML_ENTRY_UCHAR2(em_BlinkQosType_entry, SourceIp);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, SourcePort);
XML_ENTRY_UCHAR2(em_BlinkQosType_entry, DestinationIp);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, DestinationPort);
XML_ENTRY_UCHAR2(em_BlinkQosType_entry, Protocol);
XML_ENTRY_UCHAR2(em_BlinkQosType_entry, SourceMac);
XML_ENTRY_UCHAR2(em_BlinkQosType_entry, DestinationMac);
XML_ENTRY_PRIMITIVE2(em_BlinkQosType_entry, ulBitmap);
