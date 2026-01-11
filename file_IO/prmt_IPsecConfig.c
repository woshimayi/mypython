#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"
/*InternetGatewayDevice.X_CMCC_IPSecVPN.IPsecConfig.{i}.*/


struct CWMP_OP tIPsecConfigLeafOP = { NULL ,ObjIPsecConfig};


struct CWMP_OP tIPsecConfigLeafOPChilden= {getIPsecConfig,setIPsecConfig};
struct CWMP_PRMT tIPsecConfigLeafInfo[] =
{
	{"Name",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"Enable",  eCWMP_tBOOLEAN, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecType",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"RemoteSubnet",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"LocalSubnet",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"RemoteIP",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"RemoteDomain",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"ExchangeMode",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKEAuthenticationAlgorithm",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKEAuthenticationMethod",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKEEncryptionAlgorithm",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKEDHGroup",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKEIDType",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKELocalName",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKERemoteName",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKEPreshareKey",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecOutInterface",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecEncapsulationMode",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecTransform",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"ESPAuthenticationAlgorithm",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"ESPEncryptionAlgorithm",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecPFS",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IKESAPeriod",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecSATimePeriod",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecSATrafficPeriod",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"AHAuthenticationAlgorithm",  eCWMP_tSTRING, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DPDEnable",  eCWMP_tBOOLEAN, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DPDThreshold",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"DPDRetry",  eCWMP_tUINT, CWMP_WRITE|CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"ConnectionStatus",  eCWMP_tSTRING, CWMP_READ,  &tIPsecConfigLeafOPChilden, (void *)&gArea_Cmcc_Common},
};
enum eIPsecConfigLeaf
{
	eIPsecConfigName,
	eIPsecConfigEnable,
	eIPsecConfigIPSecType,
	eIPsecConfigRemoteSubnet,
	eIPsecConfigLocalSubnet,
	eIPsecConfigRemoteIP,
	eIPsecConfigRemoteDomain,
	eIPsecConfigExchangeMode,
	eIPsecConfigIKEAuthenticationAlgorithm,
	eIPsecConfigIKEAuthenticationMethod,
	eIPsecConfigIKEEncryptionAlgorithm,
	eIPsecConfigIKEDHGroup,
	eIPsecConfigIKEIDType,
	eIPsecConfigIKELocalName,
	eIPsecConfigIKERemoteName,
	eIPsecConfigIKEPreshareKey,
	eIPsecConfigIPSecOutInterface,
	eIPsecConfigIPSecEncapsulationMode,
	eIPsecConfigIPSecTransform,
	eIPsecConfigESPAuthenticationAlgorithm,
	eIPsecConfigESPEncryptionAlgorithm,
	eIPsecConfigIPSecPFS,
	eIPsecConfigIKESAPeriod,
	eIPsecConfigIPSecSATimePeriod,
	eIPsecConfigIPSecSATrafficPeriod,
	eIPsecConfigAHAuthenticationAlgorithm,
	eIPsecConfigDPDEnable,
	eIPsecConfigDPDThreshold,
	eIPsecConfigDPDRetry,
	eIPsecConfigConnectionStatus,
};
struct CWMP_LEAF tIPsecConfigLeaf[] =
{
	{&tIPsecConfigLeafInfo[eIPsecConfigName]},
	{&tIPsecConfigLeafInfo[eIPsecConfigEnable]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecType]},
	{&tIPsecConfigLeafInfo[eIPsecConfigRemoteSubnet]},
	{&tIPsecConfigLeafInfo[eIPsecConfigLocalSubnet]},
	{&tIPsecConfigLeafInfo[eIPsecConfigRemoteIP]},
	{&tIPsecConfigLeafInfo[eIPsecConfigRemoteDomain]},
	{&tIPsecConfigLeafInfo[eIPsecConfigExchangeMode]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKEAuthenticationAlgorithm]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKEAuthenticationMethod]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKEEncryptionAlgorithm]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKEDHGroup]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKEIDType]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKELocalName]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKERemoteName]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKEPreshareKey]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecOutInterface]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecEncapsulationMode]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecTransform]},
	{&tIPsecConfigLeafInfo[eIPsecConfigESPAuthenticationAlgorithm]},
	{&tIPsecConfigLeafInfo[eIPsecConfigESPEncryptionAlgorithm]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecPFS]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIKESAPeriod]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecSATimePeriod]},
	{&tIPsecConfigLeafInfo[eIPsecConfigIPSecSATrafficPeriod]},
	{&tIPsecConfigLeafInfo[eIPsecConfigAHAuthenticationAlgorithm]},
	{&tIPsecConfigLeafInfo[eIPsecConfigDPDEnable]},
	{&tIPsecConfigLeafInfo[eIPsecConfigDPDThreshold]},
	{&tIPsecConfigLeafInfo[eIPsecConfigDPDRetry]},
	{&tIPsecConfigLeafInfo[eIPsecConfigConnectionStatus]},
	{ NULL }
};


struct CWMP_PRMT tIPsecConfigLINKObjInfo[] =
{
	{"0",  eCWMP_tOBJECT,  CWMP_READ | CWMP_WRITE | CWMP_LNKLIST,  NULL, (void *)& gArea_Cmcc_Common}
};
enum eIPsecConfigLINKLeaf
{
	eIPsecConfigLINK,
};
struct CWMP_LINKNODE tIPsecConfigLINKObject[] =
{
	{ &tIPsecConfigLINKObjInfo[eIPsecConfigLINK],  tIPsecConfigLeaf,  NULL,       NULL,           0},
	{ NULL }
};
int setIPsecConfig(char *name, struct CWMP_LEAF *entity, int type, void *data)
{
	char	*lastname = entity->info->name;
	char	*buf = data;
	unsigned int msgLen = 0;
	IgdIPsecConfigTab stPara;
	IgdIPsecConfigTab *pstPara = &stPara;
	unsigned int  instnum = 0;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));
	instnum = getCMCC_InstNum(name);
	if (instnum == 0)
		return ERR_9005;
	pstPara->ulIndex = instnum;
	printf("<%s:%d>Index[%#x]\n", __FUNCTION__, __LINE__, pstPara->ulIndex);


                    if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigName].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT0_NAME;
                        HI_OS_STRCPY_S(pstPara->Name, sizeof(pstPara->Name), buf);
                    }else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigEnable].name))
                    {
                        int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT1_ENABLE;
                        pstPara->Enable = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecType].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT2_IPSECTYPE;
                        HI_OS_STRCPY_S(pstPara->IPSecType, sizeof(pstPara->IPSecType), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigRemoteSubnet].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT3_REMOTESUBNET;
                        HI_OS_STRCPY_S(pstPara->RemoteSubnet, sizeof(pstPara->RemoteSubnet), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigLocalSubnet].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT4_LOCALSUBNET;
                        HI_OS_STRCPY_S(pstPara->LocalSubnet, sizeof(pstPara->LocalSubnet), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigRemoteIP].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT5_REMOTEIP;
                        HI_OS_STRCPY_S(pstPara->RemoteIP, sizeof(pstPara->RemoteIP), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigRemoteDomain].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT6_REMOTEDOMAIN;
                        HI_OS_STRCPY_S(pstPara->RemoteDomain, sizeof(pstPara->RemoteDomain), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigExchangeMode].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT7_EXCHANGEMODE;
                        HI_OS_STRCPY_S(pstPara->ExchangeMode, sizeof(pstPara->ExchangeMode), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEAuthenticationAlgorithm].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT8_IKEAUTHENTICATIONALGORITHM;
                        HI_OS_STRCPY_S(pstPara->IKEAuthenticationAlgorithm, sizeof(pstPara->IKEAuthenticationAlgorithm), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEAuthenticationMethod].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT9_IKEAUTHENTICATIONMETHOD;
                        HI_OS_STRCPY_S(pstPara->IKEAuthenticationMethod, sizeof(pstPara->IKEAuthenticationMethod), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEEncryptionAlgorithm].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT10_IKEENCRYPTIONALGORITHM;
                        HI_OS_STRCPY_S(pstPara->IKEEncryptionAlgorithm, sizeof(pstPara->IKEEncryptionAlgorithm), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEDHGroup].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT11_IKEDHGROUP;
                        HI_OS_STRCPY_S(pstPara->IKEDHGroup, sizeof(pstPara->IKEDHGroup), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEIDType].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT12_IKEIDTYPE;
                        HI_OS_STRCPY_S(pstPara->IKEIDType, sizeof(pstPara->IKEIDType), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKELocalName].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT13_IKELOCALNAME;
                        HI_OS_STRCPY_S(pstPara->IKELocalName, sizeof(pstPara->IKELocalName), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKERemoteName].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT14_IKEREMOTENAME;
                        HI_OS_STRCPY_S(pstPara->IKERemoteName, sizeof(pstPara->IKERemoteName), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEPreshareKey].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT15_IKEPRESHAREKEY;
                        HI_OS_STRCPY_S(pstPara->IKEPreshareKey, sizeof(pstPara->IKEPreshareKey), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecOutInterface].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT16_IPSECOUTINTERFACE;
                        HI_OS_STRCPY_S(pstPara->IPSecOutInterface, sizeof(pstPara->IPSecOutInterface), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecEncapsulationMode].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT17_IPSECENCAPSULATIONMODE;
                        HI_OS_STRCPY_S(pstPara->IPSecEncapsulationMode, sizeof(pstPara->IPSecEncapsulationMode), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecTransform].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT18_IPSECTRANSFORM;
                        HI_OS_STRCPY_S(pstPara->IPSecTransform, sizeof(pstPara->IPSecTransform), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigESPAuthenticationAlgorithm].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT19_ESPAUTHENTICATIONALGORITHM;
                        HI_OS_STRCPY_S(pstPara->ESPAuthenticationAlgorithm, sizeof(pstPara->ESPAuthenticationAlgorithm), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigESPEncryptionAlgorithm].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT20_ESPENCRYPTIONALGORITHM;
                        HI_OS_STRCPY_S(pstPara->ESPEncryptionAlgorithm, sizeof(pstPara->ESPEncryptionAlgorithm), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecPFS].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT21_IPSECPFS;
                        HI_OS_STRCPY_S(pstPara->IPSecPFS, sizeof(pstPara->IPSecPFS), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKESAPeriod].name))
                    {
                        
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 4294967295 )
		{
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT22_IKESAPERIOD;
                        pstPara->IKESAPeriod = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecSATimePeriod].name))
                    {
                        
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 4294967295 )
		{
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT23_IPSECSATIMEPERIOD;
                        pstPara->IPSecSATimePeriod = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecSATrafficPeriod].name))
                    {
                        
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 4294967295 )
		{
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT24_IPSECSATRAFFICPERIOD;
                        pstPara->IPSecSATrafficPeriod = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigAHAuthenticationAlgorithm].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT25_AHAUTHENTICATIONALGORITHM;
                        HI_OS_STRCPY_S(pstPara->AHAuthenticationAlgorithm, sizeof(pstPara->AHAuthenticationAlgorithm), buf);
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigDPDEnable].name))
                    {
                        int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT26_DPDENABLE;
                        pstPara->DPDEnable = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigDPDThreshold].name))
                    {
                        
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 4294967295 )
		{
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT27_DPDTHRESHOLD;
                        pstPara->DPDThreshold = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigDPDRetry].name))
                    {
                        
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < 0 || *i > 4294967295 )
		{
		    return ERR_9007;
		}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT28_DPDRETRY;
                        pstPara->DPDRetry = *(unsigned int *)buf;
                    }
                    else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigConnectionStatus].name))
                    {
                        if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= 128) {
			return ERR_9007;
       	}

                        pstPara->ulBitmap = IPSECCONFIG_ATTR_MASK_BIT29_CONNECTIONSTATUS;
                        HI_OS_STRCPY_S(pstPara->ConnectionStatus, sizeof(pstPara->ConnectionStatus), buf);
                    }
                    
	msgLen = sizeof(stPara);
	CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_IPSECCONFIG_TAB, (UINT8 *)pstPara, 0, msgLen);
	return 0;
}

int getIPsecConfig(char *name, struct CWMP_LEAF *entity, int *type, void **data)
{
	char	*lastname = entity->info->name;
	unsigned int msgLen = 0;
    unsigned int  instnum = 0;
    
	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	IgdIPsecConfigTab stPara;
	IgdIPsecConfigTab *pstPara = &stPara;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));
	PP("name = %s", name);
	instnum = getCMCC_InstNum(name);
	PP("instnum = %d", instnum);
	if (instnum == 0)
		return ERR_9005;
	pstPara->ulIndex = instnum;

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_LIST_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_IPSECCONFIG_TAB, (UINT8 *)pstPara, 0, msgLen);
	
	*type = entity->info->type;
	*data = NULL;

	if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigName].name))
	{
		*data = strdup(pstPara->Name);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigEnable].name))
	{
		*data = booldup(pstPara->Enable);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecType].name))
	{
		*data = strdup(pstPara->IPSecType);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigRemoteSubnet].name))
	{
		*data = strdup(pstPara->RemoteSubnet);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigLocalSubnet].name))
	{
		*data = strdup(pstPara->LocalSubnet);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigRemoteIP].name))
	{
		*data = strdup(pstPara->RemoteIP);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigRemoteDomain].name))
	{
		*data = strdup(pstPara->RemoteDomain);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigExchangeMode].name))
	{
		*data = strdup(pstPara->ExchangeMode);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEAuthenticationAlgorithm].name))
	{
		*data = strdup(pstPara->IKEAuthenticationAlgorithm);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEAuthenticationMethod].name))
	{
		*data = strdup(pstPara->IKEAuthenticationMethod);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEEncryptionAlgorithm].name))
	{
		*data = strdup(pstPara->IKEEncryptionAlgorithm);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEDHGroup].name))
	{
		*data = strdup(pstPara->IKEDHGroup);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEIDType].name))
	{
		*data = strdup(pstPara->IKEIDType);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKELocalName].name))
	{
		*data = strdup(pstPara->IKELocalName);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKERemoteName].name))
	{
		*data = strdup(pstPara->IKERemoteName);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKEPreshareKey].name))
	{
		*data = strdup(pstPara->IKEPreshareKey);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecOutInterface].name))
	{
		*data = strdup(pstPara->IPSecOutInterface);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecEncapsulationMode].name))
	{
		*data = strdup(pstPara->IPSecEncapsulationMode);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecTransform].name))
	{
		*data = strdup(pstPara->IPSecTransform);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigESPAuthenticationAlgorithm].name))
	{
		*data = strdup(pstPara->ESPAuthenticationAlgorithm);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigESPEncryptionAlgorithm].name))
	{
		*data = strdup(pstPara->ESPEncryptionAlgorithm);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecPFS].name))
	{
		*data = strdup(pstPara->IPSecPFS);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIKESAPeriod].name))
	{
		*data = uintdup(pstPara->IKESAPeriod);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecSATimePeriod].name))
	{
		*data = uintdup(pstPara->IPSecSATimePeriod);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigIPSecSATrafficPeriod].name))
	{
		*data = uintdup(pstPara->IPSecSATrafficPeriod);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigAHAuthenticationAlgorithm].name))
	{
		*data = strdup(pstPara->AHAuthenticationAlgorithm);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigDPDEnable].name))
	{
		*data = booldup(pstPara->DPDEnable);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigDPDThreshold].name))
	{
		*data = uintdup(pstPara->DPDThreshold);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigDPDRetry].name))
	{
		*data = uintdup(pstPara->DPDRetry);
	}
	else if (!strcmp(lastname, tIPsecConfigLeafInfo[eIPsecConfigConnectionStatus].name))
	{
		*data = strdup(pstPara->ConnectionStatus);
	}
	else
	{
		return ERR_9005;
	}
	return 0;
}
       
int ObjIPsecConfig(char *name, struct CWMP_LEAF *e, int type, void *data)
{
	struct CWMP_NODE *entity = (struct CWMP_NODE *)e;
	unsigned int ulloop;
	unsigned int msgLen = 0;
	 int ret;
	IgdIPsecConfigTab stPara;
	IgdIPsecConfigTab *pstPara = &stPara;
	IgdIPsecConfigTab *pstParaList = NULL;
	uint32_t *index;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));
	type = (type == eCWMP_tINITOBJ)?eCWMP_tUPDATEOBJ:type;

	switch( type )
	{
	case eCWMP_tINITOBJ:
		 {
			unsigned int MaxInstNum = 0;
			struct CWMP_LINKNODE **table = (struct CWMP_LINKNODE **)data;

			if( (name==NULL) || (entity==NULL) || (data==NULL) ) return -1;

		  CWMP_API_GET_ENTRY_CNT_FUNC(IGD_IPSECCONFIG_TAB,&MaxInstNum);
		  CWMP_LOG(LOG_DEBUG,"INIT IGD.X_CMCC_Security.UrlFilter.obj  NUM=[%d]\n",MaxInstNum);
			if(MaxInstNum == 0)
				return 0;

			pstParaList = (IgdIPsecConfigTab *)malloc(MaxInstNum*sizeof(IgdIPsecConfigTab));
			if(NULL == pstParaList) return 0;
			HI_OS_MEMSET_S((UINT8*)pstParaList, MaxInstNum*sizeof(IgdIPsecConfigTab), 0, MaxInstNum*sizeof(IgdIPsecConfigTab));
			msgLen = MaxInstNum*sizeof(IgdIPsecConfigTab);

			CWMP_API_GET_ALL_ENTRY_FUNC(IGD_IPSECCONFIG_TAB,pstParaList,msgLen,free(pstParaList));

			for( ulloop=0; ulloop<MaxInstNum; ulloop++ )
			{
				CWMP_LOG(LOG_DEBUG,"INIT IGD.X_CMCC_Security.UrlFilter.obj	INDEX=[%d]\n",pstParaList[ulloop].ulIndex);
				if( create_Object(table, tIPsecConfigLINKObject, sizeof(tIPsecConfigLINKObject), 1, pstParaList[ulloop].ulIndex) < 0 )
				{
					 free(pstParaList);
					 return -1;
				}

			}
			//add_objectNum( name, MaxInstNum );
					 free(pstParaList);
			return 0;
		 }
	case eCWMP_tADDOBJ:
		 {
			 if( (name==NULL) || (entity==NULL) || (data==NULL) ) return -1;

			msgLen = sizeof(stPara);
			CWMP_API_ADD_ENTRY_FUNC(IGD_IPSECCONFIG_TAB,pstPara,msgLen);
			CWMP_LOG(LOG_DEBUG,"CM ADD IGD.X_CMCC_Security.UrlFilter.obj  INDEX=[%d]\n",pstPara->ulIndex);
			*(unsigned int*)data = pstPara->ulIndex;

			 ret = add_Object( name, (struct CWMP_LINKNODE **)&entity->next, tIPsecConfigLINKObject, sizeof(tIPsecConfigLINKObject), data );
			 HI_CWMP_LOG(CM_LOG_INFO_E, 1,"ADD %s .(inst:%d,ret:%x)", name, *(int*)data, ret);

			 return ret;
		 }

	case eCWMP_tDELOBJ:
		{
			pstPara->ulIndex = *(int*)data;
			msgLen = sizeof(stPara);
			CWMP_API_DEL_ENTRY_FUNC(IGD_IPSECCONFIG_TAB,pstPara,msgLen);

			ret = del_Object( name, (struct CWMP_LINKNODE **)&entity->next, *(int*)data );
			 HI_CWMP_LOG(CM_LOG_INFO_E,1, "ADD %s .(inst:%d,ret:%x)", name, *(int*)data, ret);

			return ret;
		}
	case eCWMP_tUPDATEOBJ:
		{
			unsigned int num=0, i, ulIndex = 0;
			struct CWMP_LINKNODE *old_table;

			CWMP_API_GET_ENTRY_CNT_FUNC(IGD_IPSECCONFIG_TAB,&num);

			CWMPDBG( 1, ( stderr, "<%s:%d>[DEBUG]:table_count is %d\n", __FUNCTION__, __LINE__, num) );
			if(num == 0)
				return 0;

			index = malloc(num * sizeof(uint32_t));
			if(NULL == index) return 0;
			(void)memset_s(index, num*sizeof(uint32_t), 0, num*sizeof(uint32_t));
			msgLen = num * sizeof(uint32_t);
			igdCmConfGetallIndex (IGD_IPSECCONFIG_TAB, (UINT8*)index, msgLen);

			old_table = (struct CWMP_LINKNODE *)entity->next;
			entity->next = NULL;
			for( i=0; i<num;i++ )
			{
				ulIndex = index[i];
				add_Object( name, (struct CWMP_LINKNODE **)&entity->next,  tIPsecConfigLINKObject, sizeof(tIPsecConfigLINKObject), &ulIndex );
			}
			if( old_table )
			{
				destroy_ParameterTable( (struct CWMP_NODE *)old_table );
			}
			free(index);
			return 0;
		}
	}

	return -1;
}

