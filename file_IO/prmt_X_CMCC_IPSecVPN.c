
#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"

#include "prmt_IpSecVpn.h"
/*IpSecVpn*/


struct CWMP_OP tIpSecVpnLeafOPChilden= {getIpSecVpn,setIpSecVpn};
struct CWMP_PRMT tIpSecVpnLeafInfo[] =
{
	{"MaxNumberOfEntries",  eCWMP_tUINT, CWMP_READ,  &tIpSecVpnLeafOPChilden, (void *)&gArea_Cmcc_Common},
	{"IPSecVPNNumberOfEntries",  eCWMP_tUINT, CWMP_READ,  &tIpSecVpnLeafOPChilden, (void *)&gArea_Cmcc_Common},
};
enum eIpSecVpnLeaf
{
	eIpSecVpnMaxNumberOfEntries,
	eIpSecVpnIPSecVPNNumberOfEntries,
};
struct CWMP_LEAF tIpSecVpnLeaf[] =
{
	{&tIpSecVpnLeafInfo[eIpSecVpnMaxNumberOfEntries]},
	{&tIpSecVpnLeafInfo[eIpSecVpnIPSecVPNNumberOfEntries]},
	{ NULL }
};


int setIpSecVpn(char *name, struct CWMP_LEAF *entity, int type, void *data)
{
	char *lastname = entity->info->name;
	char *buf = data;
	IgdIpSecVpnTab stPara;
	IgdIpSecVpnTab *pstPara = &stPara;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdIpSecVpnTab), 0, sizeof(IgdIpSecVpnTab));


                    if (!strcmp(lastname, tIpSecVpnLeafInfo[eIpSecVpnMaxNumberOfEntries].name))
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

                        pstPara->ulBitmap = IPSECVPN_ATTR_MASK_BIT0_MAXNUMBEROFENTRIES;
                        pstPara->MaxNumberOfEntries = *(unsigned int *)buf;
                    }else if (!strcmp(lastname, tIpSecVpnLeafInfo[eIpSecVpnIPSecVPNNumberOfEntries].name))
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

                        pstPara->ulBitmap = IPSECVPN_ATTR_MASK_BIT1_IPSECVPNNUMBEROFENTRIES;
                        pstPara->IPSecVPNNumberOfEntries = *(unsigned int *)buf;
                    }
                    else
	{
		return ERR_9005;
	}

	if (pstPara->ulBitmap)
	{
		CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_IPSECVPN_TAB,
		                                  (UINT8 *)pstPara, 0, sizeof(stPara));
	}

	return 0;
}

int getIpSecVpn(char *name, struct CWMP_LEAF *entity, int *type, void **data)
{
	char *lastname = entity->info->name;
	unsigned int msgLen = 0;
	IgdIpSecVpnTab stPara;
	IgdIpSecVpnTab *pstPara = &stPara;

	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdIpSecVpnTab), 0, sizeof(IgdIpSecVpnTab));

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_IPSECVPN_TAB,
	                                  (UINT8 *)pstPara, 0, msgLen);

	*type = entity->info->type;
	*data = NULL;

	if (!strcmp(lastname, tIpSecVpnLeafInfo[eIpSecVpnMaxNumberOfEntries].name))
	{
		*data = uintdup(pstPara->MaxNumberOfEntries);
	}
	else if (!strcmp(lastname, tIpSecVpnLeafInfo[eIpSecVpnIPSecVPNNumberOfEntries].name))
	{
		*data = uintdup(pstPara->IPSecVPNNumberOfEntries);
	}
	else
	{
		return ERR_9005;
	}
	return 0;
}
       
